import copy
import json
from pathlib import Path
import tempfile
import unittest

import localization_tools as tool


class LocalizationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def save(self, name, value):
        path = self.root / name
        path.write_bytes(tool.encoded(value))
        return path

    def row(self, ident="a", source="Hello ~INPUT_JUMP~ %2$s {name}"):
        return {"id": ident, "native_id": "native-" + ident, "source": source,
                "source_sha": tool.sha(source.encode()), "candidate": "Vecs tulkojums"}

    def edit(self, row, target="Sveiki ~INPUT_JUMP~ %2$s {name}"):
        return dict(row, target=target, decision="ready", reason="Pārskatīts")

    def run_qa(self, rows, edits):
        return tool.validate([self.save("input.json", {"rows": rows})], [self.save("edited.json", edits)])

    def codes(self, report):
        return {e["code"] for e in report["errors"]}

    def test_empty_batch_rejected(self):
        self.assertIn("empty_input", self.codes(self.run_qa([], [])))

    def test_duplicate_native_key_rejected(self):
        a = self.row("a")
        b = dict(self.row("b"), native_id=a["native_id"])
        self.assertIn("duplicate_native_id", self.codes(self.run_qa([a, b], [self.edit(a), self.edit(b)])))

    def test_literal_percent_changed(self):
        row = self.row(source="Done: %d%%")
        self.assertIn("placeholder_mismatch", self.codes(self.run_qa([row], [self.edit(row, "Gatavs: %d%")])))

    def test_valid_unicode_and_positioned_placeholders(self):
        row = self.row()
        report = self.run_qa([row], [self.edit(row)])
        self.assertTrue(report["mechanical_pass"])
        self.assertFalse(report["semantic_approval"])

    def test_missing_extra_and_duplicate_ids_block(self):
        a, b = self.row(), self.row("b")
        report = self.run_qa([a, b], [self.edit(a), self.edit(a), self.edit(self.row("c"))])
        self.assertTrue({"missing_id", "extra_id", "duplicate_edited_id"} <= self.codes(report))
        self.assertTrue(report["blocked"])

    def test_duplicate_input_ids_block(self):
        row = self.row()
        report = self.run_qa([row, row], [self.edit(row)])
        self.assertIn("duplicate_input_id", self.codes(report))

    def test_source_native_context_and_candidate_cannot_change(self):
        row = dict(self.row(), context_id="scene-1")
        for key in ["source", "source_sha", "native_id", "candidate", "context_id"]:
            with self.subTest(key=key):
                edit = self.edit(row)
                edit[key] = "changed"
                self.assertIn("changed_invariant", self.codes(self.run_qa([row], [edit])))

    def test_placeholder_missing_and_duplicate_block(self):
        row = self.row()
        for target in ["Sveiki %2$s {name}", "Sveiki ~INPUT_JUMP~ %2$s {name}{name}",
                       "Sveiki ~INPUT_JUMP~ %s {name}"]:
            self.assertIn("placeholder_mismatch", self.codes(self.run_qa([row], [self.edit(row, target)])))

    def test_printf_escaped_percent_and_precision(self):
        self.assertEqual(tool.placeholders("100%% %1$03.2f")['printf'], {"%1$03.2f": 1})
        self.assertEqual(tool.placeholders("{{literal}} {0:d}")['brace'], {"{0:d}": 1})

    def test_implicit_printf_order_cannot_change(self):
        row = self.row(source="Name %s count %d")
        report = self.run_qa([row], [self.edit(row, "Skaits %d vārds %s")])
        self.assertIn("placeholder_order_mismatch", self.codes(report))
        self.assertNotIn("placeholder_mismatch", self.codes(report))

    def test_fully_positional_printf_may_reorder(self):
        row = self.row(source="Name %1$s count %2$d")
        report = self.run_qa([row], [self.edit(row, "Skaits %2$d vārds %1$s")])
        self.assertTrue(report["mechanical_pass"])

    def test_implicit_dynamic_width_cannot_reorder(self):
        row = self.row(source="Width %1$*s count %2$d")
        report = self.run_qa([row], [self.edit(row, "Skaits %2$d platums %1$*s")])
        self.assertIn("placeholder_order_mismatch", self.codes(report))

    def test_rdr_tilde_order_cannot_change(self):
        row = self.row(source="~A~~B~Hello")
        report = self.run_qa([row], [self.edit(row, "~B~~A~Sveiki")])
        self.assertIn("placeholder_order_mismatch", self.codes(report))
        self.assertNotIn("placeholder_mismatch", self.codes(report))

    def test_extended_context_fields_are_invariant(self):
        fields = {"scene_id": "scene1", "branch_id": "branch1", "speaker_id": "speaker1",
                  "context_before": "Before", "context_after": "After",
                  "character_profile": {"role": "friend"}, "style_guide_revision": "v1"}
        row = dict(self.row(), **fields)
        for key in fields:
            edit = self.edit(row)
            del edit[key]
            with self.subTest(field=key):
                report = self.run_qa([row], [edit])
                self.assertTrue(any(e['code'] == 'changed_invariant' and e['field'] == key
                                    for e in report['errors']))
        report = tool.prepare([self.save("full_context.json", [row])], self.root / "context_packets")
        packed, _ = tool.read_rows([self.root / "context_packets" / report['packets'][0]['path']])
        for key, value in fields.items():
            self.assertEqual(packed[0][key], value)

    def test_hold_retains_issue_without_ready_acceptance(self):
        row = self.row()
        edit = dict(self.edit(row, ""), decision="hold", reason="Nepieciešams konteksts")
        report = self.run_qa([row], [edit])
        self.assertEqual(report["hold_declared"], 1)
        self.assertEqual(report["ready_declared"], 0)
        self.assertTrue(report["warnings"])
        edit["reason"] = ""
        self.assertIn("hold_reason_required", self.codes(self.run_qa([row], [edit])))

    def test_newline_and_identical_target_are_warnings(self):
        row = self.row(source="Same\ntext")
        report = self.run_qa([row], [self.edit(row, "Same text")])
        self.assertEqual(report["warnings"][0]["code"], "newline_count_changed")
        report = self.run_qa([row], [self.edit(row, row["source"])])
        self.assertIn("target_equals_source", {w["code"] for w in report["warnings"]})
        self.assertFalse(report["semantic_approval"])

    def test_prepare_exact_coverage_originals_and_limits(self):
        rows = [self.row(str(i), source="Hello " + str(i)) for i in range(7)]
        rows[0]["extra_provenance"] = {"evidence": "x" * 2000}
        source = self.save("input.json", {"rows": rows})
        before = source.read_bytes()
        output = self.root / "packets"
        report = tool.prepare([source], output, max_rows=3, max_source_chars=20)
        restored = []
        for packet in report["packets"]:
            items, _ = tool.read_rows([output / packet["path"]])
            self.assertLessEqual(len(items), 3)
            self.assertLessEqual(sum(len(r["source"]) for r in items), 20)
            restored.extend(items)
        self.assertEqual([r["id"] for r in restored], [r["id"] for r in rows])
        self.assertEqual(before, source.read_bytes())
        self.assertEqual(before, (output / report["originals"][0]["saved_path"]).read_bytes())
        self.assertGreater(report["worker_payload_reduction_fraction"], 0)
        self.assertNotIn("context_id", restored[0])
        with self.assertRaises(FileExistsError):
            tool.prepare([source], output)

    def test_prepare_rejects_input_directory_and_bad_hash(self):
        row = self.row()
        source = self.save("input.json", [row])
        with self.assertRaises(ValueError):
            tool.prepare([source], self.root)
        row["source_sha"] = "incorrect"
        self.save("input.json", [row])
        with self.assertRaises(ValueError):
            tool.prepare([source], self.root / "new")
        self.assertFalse((self.root / "new").exists())

    def tmrow(self, ident="a", context="scene1", target="Sveiki"):
        row = self.row(ident, "Hello")
        proof = self.root / "review.json"
        if not proof.exists():
            proof.write_text('{"reviewed":true}', encoding="utf-8")
        row.update(game="example", target_language="lv", context_id=context, context_revision="1",
                   policy_revision="1", terminology_revision="1", target=target,
                   target_sha=tool.sha(target.encode()), review_status="approved",
                   verified_review_reference={"path": str(proof), "sha256": tool.sha(proof.read_bytes())})
        return row

    def test_tm_conflict_blocks_key_and_unknown_context_rejected(self):
        a, b = self.tmrow(), self.tmrow("b", target="Labdien")
        missing = self.tmrow("c")
        del missing["context_id"]
        report = tool.tm_index([self.save("tm.json", [a, b, missing])])
        self.assertEqual(len(report["entries"]), 0)
        self.assertEqual(len(report["conflicts"]), 1)
        self.assertEqual(len(report["rejected"]), 1)
        self.assertFalse(report["automatic_acceptance"])

    def test_tm_different_contexts_never_collide(self):
        a, b = self.tmrow(), self.tmrow("b", context="scene2", target="Labdien")
        index = tool.tm_index([self.save("tm.json", [a, b])])
        self.assertEqual(len(index["entries"]), 2)
        self.assertFalse(index["conflicts"])
        query = copy.deepcopy(b)
        index_path = self.save("index.json", index)
        result = tool.tm_suggest([self.save("query.json", [query])], index_path)
        self.assertEqual(result["suggestions"][0]["suggested_target"], "Labdien")
        query["context_revision"] = "2"
        result = tool.tm_suggest([self.save("query.json", [query])], index_path)
        self.assertFalse(result["suggestions"])

    def test_tm_proof_and_target_hash_verified(self):
        row = self.tmrow()
        row["target_sha"] = "wrong"
        index = tool.tm_index([self.save("tm.json", [row])])
        self.assertEqual(index["rejected"][0]["code"], "target_sha_mismatch")
        row = self.tmrow()
        index = tool.tm_index([self.save("tm.json", [row])])
        index_path = self.save("index.json", index)
        (self.root / "review.json").write_text("changed")
        with self.assertRaises(ValueError):
            tool.tm_suggest([self.save("query.json", [row])], index_path)


if __name__ == "__main__":
    unittest.main()
