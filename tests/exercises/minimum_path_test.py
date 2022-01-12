import unittest
from helpers import Graph
from exercises import minimum_path


class TestMinimumPath(unittest.TestCase):
    def setUp(self):
        self.g1 = Graph([1, 2, 3], [(1, 2), (1, 3)])
        self.g2 = Graph([1, 2, 3, 4, 5],
                        [(1, 5), (2, 3), (2, 5), (3, 4), (4, 5)])

    def test_small_graph(self):
        self.assertTrue(minimum_path(self.g1, 1, 2, 1))

    def test_bigger_graph(self):
        self.assertTrue(minimum_path(self.g2, 1, 5, 1))
        self.assertFalse(minimum_path(self.g2, 1, 3, 2))
        self.assertFalse(minimum_path(self.g2, 1, 3, 3))


if __name__ == '__main__':
    unittest.main()
