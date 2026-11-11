#!/usr/bin/env python3
"""Compare two trusted RDR2 StringTable exports by game ID and exact decoded text."""

import argparse
from hashlib import sha256
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

RDR2_ID = re.compile(r"0x[0-9A-Fa-f]{8}")


def read_table(path):
    data = Path(path).read_bytes()
    root = ET.fromstring(data)
    if root.tag != "StringTable" or (root.text or "").strip():
        raise ValueError(f"{path}: expected a StringTable containing String elements")

    entries = {}
    for element in root:
        item_id = element.get("id", "")
        if (element.tag != "String" or list(element) or
                not RDR2_ID.fullmatch(item_id) or (element.tail or "").strip()):
            raise ValueError(f"{path}: unexpected element or game ID at {item_id!r}")
        key = int(item_id, 16)
        if key in entries:
            raise ValueError(f"{path}: duplicate numeric game ID {item_id}")
        if not (element.text or "").strip():
            raise ValueError(f"{path}: empty target at {item_id}")
        entries[key] = element.text
    if not entries:
        raise ValueError(f"{path}: no translated strings")
    return entries, sha256(data).hexdigest()


def compare(reference_path, copy_path):
    reference, reference_hash = read_table(reference_path)
    copy, copy_hash = read_table(copy_path)
    missing = reference.keys() - copy.keys()
    extra = copy.keys() - reference.keys()
    changed = {key for key in reference.keys() & copy.keys() if reference[key] != copy[key]}
    differences = {"missing": missing, "extra": extra, "changed": changed}
    return {
        "reference_entries": len(reference),
        "copy_entries": len(copy),
        "reference_sha256": reference_hash,
        "copy_sha256": copy_hash,
        "bytes_identical": reference_hash == copy_hash,
        "all_pairs_match": not any(differences.values()),
        "difference_counts": {name: len(keys) for name, keys in differences.items()},
        "first_10_ids": {name: [f"0x{key:08X}" for key in sorted(keys)[:10]]
                         for name, keys in differences.items()},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference", help="Reviewed complete RDR2 XML")
    parser.add_argument("copy", help="Staged release or installed XML")
    args = parser.parse_args()
    try:
        report = compare(args.reference, args.copy)
    except (OSError, ValueError, ET.ParseError) as error:
        print(str(error), file=sys.stderr)
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["all_pairs_match"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
