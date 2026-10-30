"""Tests for slugify. These tests are the spec: fix the program, not a test."""

import unittest

from slugify import slugify


class TestSlugify(unittest.TestCase):
    def test_lowercases_and_joins_with_hyphens(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_drops_punctuation(self):
        self.assertEqual(slugify("Ship it!"), "ship-it")

    def test_trims_surrounding_space(self):
        self.assertEqual(slugify("  draft  "), "draft")

    def test_collapses_runs_of_separators(self):
        self.assertEqual(slugify("Plan -- then build"), "plan-then-build")


if __name__ == "__main__":
    unittest.main()
