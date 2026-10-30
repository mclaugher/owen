import os
import tempfile
import unittest

import todo


class TodoTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self._old_cwd = os.getcwd()
        os.chdir(self._tmp.name)

    def tearDown(self):
        os.chdir(self._old_cwd)
        self._tmp.cleanup()

    def test_list_without_data_says_nothing_to_do(self):
        self.assertEqual(todo.format_list(), "nothing to do")

    def test_add_then_list_shows_the_item_open(self):
        todo.add("review the diff")
        self.assertEqual(todo.format_list(), "1  [ ] review the diff")

    def test_done_marks_the_numbered_item(self):
        todo.add("write the plan")
        todo.add("review the diff")
        todo.done(1)
        self.assertEqual(
            todo.format_list().splitlines(),
            ["1  [x] write the plan", "2  [ ] review the diff"],
        )

    def test_done_out_of_range_changes_nothing(self):
        todo.add("write the plan")
        self.assertEqual(todo.done(9), "no item 9")
        self.assertEqual(todo.format_list(), "1  [ ] write the plan")


if __name__ == "__main__":
    unittest.main()
