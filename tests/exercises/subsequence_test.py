import unittest
from exercises import subsequence


class TestSubsequence(unittest.TestCase):
    def test_empty_array(self):
        self.assertFalse(subsequence([], 100))

    def test_only_distinct_values(self):
        self.assertTrue(subsequence([1, 2, 3, 4, 5, 6], 0))  # e.g. []
        self.assertFalse(subsequence([1, 2, 3, 4, 5, 6], 10))

    def test_duplicated_values(self):
        self.assertTrue(subsequence([1, 2, 2, 2, 90, 90, 4], 2))  # e.g. [2, 2]
        self.assertFalse(subsequence([1, 2, 2, 2, 90, 90, 4], 3))


if __name__ == '__main__':
    unittest.main()
