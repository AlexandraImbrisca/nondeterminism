import unittest
from exercises import q_sums


class TestQSums(unittest.TestCase):
    def test_empty_array(self):
        self.assertFalse(q_sums([], 100))

    def test_no_sum(self):
        self.assertFalse(q_sums([1, 2, 100, 98], 5))
        self.assertFalse(q_sums([1, -2, 3, -4, -5], -12))

    def test_existing_sum(self):
        self.assertTrue(q_sums([1, 2, 100, 98], 99))
        self.assertTrue(q_sums([1, -2, 3, -4, -5], -8))


if __name__ == '__main__':
    unittest.main()
