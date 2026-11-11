from pathlib import Path
import tempfile
import unittest

from compare_xml import compare, read_table


class XmlTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.one = '<String id="0xABCDEF01">Jā &amp; nē</String>'
        self.two = '<String id="0xABCDEF02">Aiziet!</String>'

    def xml(self, filename, body):
        path = self.root / filename
        path.write_text("<StringTable>" + body + "</StringTable>", encoding="utf-8")
        return path

    def test_equal_pairs_ignore_order_and_numeric_key_case(self):
        original = self.xml("a.xml", self.one + self.two)
        installed = self.xml("b.xml", self.two + self.one.replace("ABCDEF01", "abcdef01"))
        report = compare(original, installed)
        self.assertTrue(report["all_pairs_match"])
        self.assertFalse(report["bytes_identical"])

    def test_changed_missing_and_extra_ids(self):
        report = compare(self.xml("a.xml", self.one + self.two),
                         self.xml("b.xml", self.one.replace("Jā", "Nē") + self.two.replace("02", "03")))
        self.assertEqual(report["difference_counts"], {"missing": 1, "extra": 1, "changed": 1})

    def test_duplicate_empty_and_nested_are_rejected(self):
        for body in (self.one * 2, self.one + self.one.replace("ABCDEF01", "abcdef01"),
                     "", self.one.replace("Jā &amp; nē", " "), self.one.replace("Jā", "<b>Jā</b>")):
            with self.subTest(body=body), self.assertRaises(ValueError):
                read_table(self.xml("bad.xml", body))


if __name__ == "__main__":
    unittest.main()
