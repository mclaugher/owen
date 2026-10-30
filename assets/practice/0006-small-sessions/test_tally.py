import os
import tempfile
import unittest

import tally


class TallyTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self._old_cwd = os.getcwd()
        os.chdir(self._tmp.name)

    def tearDown(self):
        os.chdir(self._old_cwd)
        self._tmp.cleanup()

    def test_list_without_data_says_no_entries(self):
        self.assertEqual(tally.format_list(), "no entries")

    def test_add_then_list_shows_the_entry(self):
        tally.add(4.60, "coffee", "flat white")
        self.assertEqual(tally.format_list(), "    4.60  coffee  (flat white)")

    def test_add_appends_in_order(self):
        tally.add(4.60, "coffee")
        tally.add(12.00, "lunch")
        self.assertEqual(
            tally.format_list().splitlines(),
            ["    4.60  coffee", "   12.00  lunch"],
        )

    def test_amounts_keep_two_decimals(self):
        tally.add(5, "coffee")
        self.assertTrue(tally.format_list().startswith("    5.00"))


if __name__ == "__main__":
    unittest.main()
