import unittest
from examples import sort


class TestSortPositiveArray(unittest.TestCase):
    def test_sort_valid_values(self):
        self.assertTrue(sort([1, 100, 6, 20]))

    def test_sort_invalid_values(self):
        self.assertFalse(sort([0, 10000, 1, -10, 6, 0]))


if __name__ == '__main__':
    unittest.main()
