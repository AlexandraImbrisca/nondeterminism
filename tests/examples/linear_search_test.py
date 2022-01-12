import unittest
from examples import linear_search


class TestLinearSearch(unittest.TestCase):
    def test_empty_array(self):
        self.assertFalse(linear_search([], 1))

    def test_element_not_found(self):
        self.assertFalse(linear_search([1, 2, 3, 4], -10))
        self.assertFalse(linear_search(list(range(10000)), 12345))

    def test_element_found(self):
        self.assertTrue(linear_search([1, 2, 3, 4], 3))
        self.assertTrue(linear_search(list(range(10000)), 1000))


if __name__ == '__main__':
    unittest.main()
