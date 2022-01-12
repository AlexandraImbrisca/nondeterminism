import unittest
from exercises import partition


class TestPartition(unittest.TestCase):
    def test_empty_array(self):
        self.assertTrue(partition([]))

    def test_no_partition(self):
        self.assertFalse(partition([1, -10, 100]))
        self.assertFalse(partition([1, 2, 3, 5]))

    def test_existing_partition(self):
        self.assertTrue(partition([1, 2, 3, 4]))
        self.assertTrue(partition([1, 10, 90, 81]))


if __name__ == '__main__':
    unittest.main()
