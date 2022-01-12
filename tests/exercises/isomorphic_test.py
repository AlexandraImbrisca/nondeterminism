import unittest
from helpers import Graph
from exercises import isomorphic


class TestIsomorphicGraphs(unittest.TestCase):
    def setUp(self):
        self.g1 = Graph([1, 2, 3], [(1, 2), (1, 3)])
        self.g2 = Graph([1, 2, 3], [(1, 2), (2, 3)])

        self.g3 = Graph([1, 2, 3, 4, 5], [(1, 2), (3, 4), (3, 5), (4, 5)])
        self.g4 = Graph([1, 2, 3, 4, 5], [(1, 2), (1, 3), (3, 5), (2, 4)])

    def test_not_isomorphic_graphs(self):
        self.assertFalse(isomorphic(self.g1, self.g3))
        self.assertFalse(isomorphic(self.g3, self.g4))

    def test_isomorphic_graphs(self):
        self.assertTrue(isomorphic(self.g1, self.g2))


if __name__ == '__main__':
    unittest.main()
