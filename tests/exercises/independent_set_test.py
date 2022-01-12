import unittest
from helpers import Graph
from exercises import independent_set


class TestIndependentSet(unittest.TestCase):
    def setUp(self):
        self.g1 = Graph([1, 2, 3], [(1, 2), (1, 3)])
        self.g2 = Graph([1, 2, 3, 4, 5],
                        [(1, 5), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5)])

    def test_small_graph(self):
        self.assertTrue(independent_set(self.g1, 1))  # e.g. S = [1]
        self.assertTrue(independent_set(self.g1, 2))  # e.g. S = [1, 3]
        self.assertFalse(independent_set(self.g1, 3))

    def test_bigger_graph(self):
        self.assertTrue(independent_set(self.g2, 1))  # e.g. S = [1]
        self.assertTrue(independent_set(self.g2, 2))  # e.g. S = [1, 4]
        self.assertTrue(independent_set(self.g2, 3))  # e.g. S = [1, 2, 4]
        self.assertFalse(independent_set(self.g2, 4))


if __name__ == '__main__':
    unittest.main()
