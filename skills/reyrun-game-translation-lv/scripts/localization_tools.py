#!/usr/bin/env python3
"""Read-only localization preparation, mechanical QA and reviewed-TM suggestions.

Never invokes a model, modifies inputs, approves language quality or deploys a game.
Output directories/files are exclusive. Reuse of a TM remains a suggestion.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
import sys

VERSION = "1.1.0"
REQUIRED = ("id", "source", "source_sha", "candidate")
INVARIANTS = REQUIRED + ("native_id",)
CONTEXT = ("context", "context_id", "context_revision", "game", "game_version",
           "version", "speaker", "target_language", "policy_revision",
           "terminology_revision", "scene_id", "branch_id", "speaker_id",
           "context_before", "context_after", "character_profile", "style_guide_revision")
TM_KEY = ("game", "target_language", "source_sha", "context_id",
          "context_revision", "policy_revision", "terminology_revision")
# Project adapters should add engine-specific syntax rather than assume every brace
# is a placeholder. These intentionally cover common simple placeholder forms.
TILDE = re.compile(r"~[^~\r\n]+~")
PRINTF = re.compile(r"%(?:\d+\$)?[-+#0 ']*(?:\d+|\*(?:\d+\$)?)?(?:\.(?:\d+|\*(?:\d+\$)?))?(?:hh|ll|[hljztL])?[diuoxXfFeEgGaAcspn]")
BRACE = re.compile(r"(?<!\{)\{(?:[A-Za-z_][\w.]*|\d+)(?:![rsa])?(?::[^{}\r\n]+)?\}(?!\})")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def encoded(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n").encode("utf-8")


def write_exclusive(path: Path, data: bytes):
    with path.open("xb") as stream:
        stream.write(data)
    if path.read_bytes() != data:
        raise ValueError("Output readback mismatch: " + str(path))


def read_rows(paths):
    rows, originals = [], []
    for name in paths:
        path = Path(name).resolve()
        raw = path.read_bytes()
        if path.suffix.lower() == ".jsonl":
            value = [json.loads(line) for line in raw.decode("utf-8-sig").splitlines() if line.strip()]
        else:
            value = json.loads(raw.decode("utf-8-sig"))
            if isinstance(value, dict):
                value = value.get("rows")
        if not isinstance(value, list) or not all(isinstance(row, dict) for row in value):
            raise ValueError("Expected a row list or object with rows: " + str(path))
        rows.extend(value)
        originals.append((path, raw))
    return rows, originals


def input_errors(rows):
    errors, seen, native_ids = [], set(), set()
    if not rows:
        errors.append({"code": "empty_input"})
    for index, row in enumerate(rows):
        ident = row.get("id")
        if not isinstance(ident, str) or not ident:
            errors.append({"index": index, "code": "invalid_id"})
            continue
        if ident in seen:
            errors.append({"id": ident, "code": "duplicate_input_id"})
        seen.add(ident)
        for key in REQUIRED:
            if not isinstance(row.get(key), str):
                errors.append({"id": ident, "code": "invalid_input_field", "field": key})
        if isinstance(row.get("source"), str) and sha(row["source"].encode()) != row.get("source_sha"):
            errors.append({"id": ident, "code": "source_sha_mismatch"})
        if "native_id" in row:
            native_id = row["native_id"]
            if not isinstance(native_id, str) or not native_id:
                errors.append({"id": ident, "code": "invalid_native_id"})
            elif native_id in native_ids:
                errors.append({"id": ident, "code": "duplicate_native_id"})
            else:
                native_ids.add(native_id)
    return errors


def prepare(paths, output, max_rows=128, max_source_chars=12000):
    if max_rows < 1 or max_source_chars < 1:
        raise ValueError("Positive packet limits required")
    rows, originals = read_rows(paths)
    errors = input_errors(rows)
    if errors:
        raise ValueError(json.dumps({"input_errors": errors}, ensure_ascii=False))
    out = Path(output).resolve()
    if any(out == path.parent or out == path for path, _ in originals):
        raise ValueError("Output must be a separate new directory")
    # Exclusive directory refuses both accidental overwrite and ambiguous resume.
    out.mkdir(parents=True, exist_ok=False)
    (out / "originals").mkdir()
    refs = []
    for i, (path, raw) in enumerate(originals):
        rel = "originals/" + str(i).zfill(4) + path.suffix
        write_exclusive(out / rel, raw)
        refs.append({"input_name": path.name, "saved_path": rel, "sha256": sha(raw), "bytes": len(raw)})
    chunks, current, chars = [], [], 0
    for row in rows:
        n = len(row["source"])
        if current and (len(current) >= max_rows or chars + n > max_source_chars):
            chunks.append(current)
            current, chars = [], 0
        current.append({k: row[k] for k in INVARIANTS + CONTEXT if k in row})
        chars += n
    if current:
        chunks.append(current)
    packets, ordered_ids, total_bytes = [], [], 0
    for i, chunk in enumerate(chunks):
        name = "packet_" + str(i).zfill(4) + ".jsonl"
        raw = b"".join(encoded(row) for row in chunk)
        write_exclusive(out / name, raw)
        ids = [row["id"] for row in chunk]
        ordered_ids.extend(ids)
        total_bytes += len(raw)
        packets.append({"path": name, "sha256": sha(raw), "bytes": len(raw), "rows": len(chunk),
                        "source_chars": sum(len(r["source"]) for r in chunk),
                        "oversize_singleton": len(chunk) == 1 and len(chunk[0]["source"]) > max_source_chars,
                        "ids_sha256": sha(encoded(ids))})
    assert ordered_ids == [r["id"] for r in rows] and len(ordered_ids) == len(set(ordered_ids))
    original_bytes = sum(len(raw) for _, raw in originals)
    report = {"tool_version": VERSION, "operation": "prepare", "rows": len(rows),
              "originals": refs, "packets": packets, "coverage_exact_disjoint": True,
              "original_input_bytes": original_bytes, "worker_packet_bytes": total_bytes,
              "worker_payload_reduction_fraction": 1 - total_bytes / original_bytes if original_bytes else None,
              "size_note": "Worker payload comparison only. Original bytes are retained; disk usage is not reduced.",
              "semantic_approval": False, "game_writes": 0}
    write_exclusive(out / "manifest.json", encoded(report))
    return report


def placeholders(text):
    # %% is a printf literal percent, not an argument placeholder.
    printf_text = text.replace("%%", "")
    return {"rdr_tilde": Counter(TILDE.findall(text)),
            "printf": Counter(PRINTF.findall(printf_text)),
            "printf_literal_percent": Counter({"%%": text.count("%%")}) if "%%" in text else Counter(),
            "brace": Counter(BRACE.findall(text))}


def ordered_placeholders(text):
    printf = PRINTF.findall(text.replace("%%", ""))
    # Only fully positional conversions may be reordered. If any conversion or
    # dynamic width/precision consumes an implicit argument, preserve the entire
    # printf sequence so mixed explicit/implicit formats fail closed as well.
    implicit = any(not re.match(r"%\d+\$", token)
                   or re.search(r"\*(?!\d+\$)", token) for token in printf)
    return {"rdr_tilde": TILDE.findall(text),
            "printf_implicit": printf if implicit else None}


def validate(input_paths, edited_paths):
    original, _ = read_rows(input_paths)
    edited, _ = read_rows(edited_paths)
    errors = input_errors(original)
    warnings, by_id = [], {}
    for i, row in enumerate(edited):
        ident = row.get("id")
        if not isinstance(ident, str) or not ident:
            errors.append({"index": i, "code": "invalid_edited_id"})
        elif ident in by_id:
            errors.append({"id": ident, "code": "duplicate_edited_id"})
        else:
            by_id[ident] = row
    original_ids = {r.get("id") for r in original if isinstance(r.get("id"), str)}
    for ident in sorted(original_ids - by_id.keys()):
        errors.append({"id": ident, "code": "missing_id"})
    for ident in sorted(by_id.keys() - original_ids):
        errors.append({"id": ident, "code": "extra_id"})
    ready = hold = 0
    for source in original:
        ident = source.get("id")
        if not isinstance(ident, str) or ident not in by_id:
            continue
        row = by_id[ident]
        for key in INVARIANTS + CONTEXT:
            if (key in source) != (key in row) or source.get(key) != row.get(key):
                errors.append({"id": ident, "code": "changed_invariant", "field": key})
        decision, target, reason = row.get("decision"), row.get("target"), row.get("reason")
        if decision not in ("ready", "hold"):
            errors.append({"id": ident, "code": "invalid_decision"})
        elif decision == "hold":
            hold += 1
            if not isinstance(reason, str) or not reason.strip():
                errors.append({"id": ident, "code": "hold_reason_required"})
        else:
            ready += 1
        if not isinstance(target, str):
            errors.append({"id": ident, "code": "target_not_text"})
            continue
        if decision == "ready" and not target.strip():
            errors.append({"id": ident, "code": "empty_ready_target"})
        if not isinstance(source.get("source"), str):
            continue
        original_text = source["source"]
        a, b = placeholders(original_text), placeholders(target)
        for kind in a:
            if a[kind] != b[kind]:
                issue = {"id": ident, "code": "placeholder_mismatch", "kind": kind,
                         "missing": dict(a[kind] - b[kind]), "extra": dict(b[kind] - a[kind])}
                (errors if decision == "ready" else warnings).append(issue)
        order_a, order_b = ordered_placeholders(original_text), ordered_placeholders(target)
        for kind in order_a:
            if order_a[kind] != order_b[kind]:
                issue = {"id": ident, "code": "placeholder_order_mismatch", "kind": kind}
                (errors if decision == "ready" else warnings).append(issue)
        if original_text.count("\n") != target.count("\n"):
            warnings.append({"id": ident, "code": "newline_count_changed"})
        if original_text == target:
            warnings.append({"id": ident, "code": "target_equals_source"})
        if target.strip() != target:
            warnings.append({"id": ident, "code": "outer_whitespace"})
    return {"tool_version": VERSION, "operation": "validate", "input_rows": len(original),
            "edited_rows": len(edited), "ready_declared": ready, "hold_declared": hold,
            "mechanical_pass": not errors, "blocked": bool(errors), "errors": errors,
            "warnings": warnings, "semantic_approval": False, "game_writes": 0}


def tm_key(row):
    if any(not isinstance(row.get(k), str) or not row[k].strip() for k in TM_KEY):
        return None
    # Exact version and speaker remain part of matching when supplied. A missing
    # context is never synthesized from an ID, position or neighbouring line.
    return tuple(row[k] for k in TM_KEY) + (row.get("game_version", row.get("version", "")), row.get("speaker", ""))


def tm_index(paths):
    rows, _ = read_rows(paths)
    groups, rejected = defaultdict(list), []
    for i, row in enumerate(rows):
        key = tm_key(row)
        if key is None:
            rejected.append({"index": i, "code": "explicit_context_or_revision_missing"})
            continue
        if row.get("review_status") != "approved":
            rejected.append({"index": i, "code": "not_explicitly_reviewed"})
            continue
        if not isinstance(row.get("source"), str) or sha(row["source"].encode()) != row["source_sha"]:
            rejected.append({"index": i, "code": "source_sha_mismatch"})
            continue
        if not isinstance(row.get("target"), str) or not row["target"].strip() or sha(row["target"].encode()) != row.get("target_sha"):
            rejected.append({"index": i, "code": "target_sha_mismatch"})
            continue
        ref = row.get("verified_review_reference")
        try:
            if not isinstance(ref, dict) or not isinstance(ref.get("path"), str) or sha(Path(ref["path"]).read_bytes()) != ref.get("sha256"):
                raise ValueError("invalid review reference")
        except (OSError, ValueError):
            rejected.append({"index": i, "code": "review_reference_unverified"})
            continue
        groups[key].append(row)
    entries, conflicts = [], []
    for key, values in sorted(groups.items()):
        if len({r["target"] for r in values}) != 1:
            conflicts.append({"key": list(key), "code": "conflicting_reviewed_targets", "records": len(values)})
        else:
            entries.append({"key": list(key), "source": values[0]["source"], "target": values[0]["target"],
                            "target_sha": values[0]["target_sha"],
                            "review_references": [r["verified_review_reference"] for r in values]})
    return {"tool_version": VERSION, "operation": "tm_index", "entries": entries,
            "conflicts": conflicts, "rejected": rejected, "automatic_acceptance": False,
            "review_reference_note": "Reference bytes verified; this tool does not judge the referenced review's linguistic validity."}


def tm_suggest(input_paths, index_path):
    rows, _ = read_rows(input_paths)
    index = json.loads(Path(index_path).read_text(encoding="utf-8"))
    if index.get("operation") != "tm_index" or index.get("automatic_acceptance") is not False:
        raise ValueError("Not a suggestions-only TM index")
    blocked = {tuple(x["key"]) for x in index["conflicts"]}
    entries = {}
    for entry in index["entries"]:
        key = tuple(entry["key"])
        if key in entries:
            blocked.add(key)
        entries[key] = entry
    suggestions, misses = [], []
    for row in rows:
        key = tm_key(row)
        entry = entries.get(key)
        if key is None or key in blocked or entry is None:
            misses.append({"id": row.get("id"), "reason": "no_unambiguous_exact_context_match"})
            continue
        if entry["source"] != row.get("source") or sha(entry["source"].encode()) != row.get("source_sha") or sha(entry["target"].encode()) != entry["target_sha"]:
            raise ValueError("Corrupt TM entry or source binding")
        # Recheck references at use time; an index is not permanent permission.
        refs = entry.get("review_references")
        if not isinstance(refs, list) or not refs or not all(
                isinstance(ref, dict) and isinstance(ref.get("path"), str)
                and sha(Path(ref["path"]).read_bytes()) == ref.get("sha256") for ref in refs):
            raise ValueError("TM review reference changed")
        suggestions.append({"id": row.get("id"), "suggested_target": entry["target"],
                            "review_references": entry["review_references"], "automatic_acceptance": False})
    return {"operation": "tm_suggest", "suggestions": suggestions, "misses": misses,
            "automatic_acceptance": False, "game_writes": 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    prep = sub.add_parser("prepare")
    prep.add_argument("inputs", nargs="+")
    prep.add_argument("--output", required=True)
    prep.add_argument("--max-rows", type=int, default=128)
    prep.add_argument("--max-source-chars", type=int, default=12000)
    qa = sub.add_parser("validate")
    qa.add_argument("--inputs", nargs="+", required=True)
    qa.add_argument("--edited", nargs="+", required=True)
    qa.add_argument("--report")
    tm = sub.add_parser("tm-index")
    tm.add_argument("inputs", nargs="+")
    tm.add_argument("--output", required=True)
    suggest = sub.add_parser("tm-suggest")
    suggest.add_argument("inputs", nargs="+")
    suggest.add_argument("--index", required=True)
    suggest.add_argument("--output", required=True)
    args = parser.parse_args()
    if args.command == "prepare":
        result = prepare(args.inputs, args.output, args.max_rows, args.max_source_chars)
    elif args.command == "validate":
        result = validate(args.inputs, args.edited)
        if args.report:
            write_exclusive(Path(args.report), encoded(result))
    elif args.command == "tm-index":
        result = tm_index(args.inputs)
        write_exclusive(Path(args.output), encoded(result))
    else:
        result = tm_suggest(args.inputs, args.index)
        write_exclusive(Path(args.output), encoded(result))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if result.get("blocked") else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(json.dumps({"error": str(error), "semantic_approval": False}), file=sys.stderr)
        raise SystemExit(2)
