import unittest
from helpers import Graph
from exercises import k_clique


class TestKClique(unittest.TestCase):
    def setUp(self):
        self.g1 = Graph([1, 2, 3], [(1, 2), (1, 3), (2, 3)])
        self.g2 = Graph([1, 2, 3, 4, 5],
                        [(1, 5), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5)])

    def test_small_graph(self):
        self.assertTrue(k_clique(self.g1, 1))  # e.g. [1]
        self.assertTrue(k_clique(self.g1, 2))  # e.g. [1, 2]
        self.assertTrue(k_clique(self.g1, 3))  # e.g. [1, 2, 3]
        self.assertFalse(k_clique(self.g1, 4))

    def test_bigger_graph(self):
        self.assertTrue(k_clique(self.g2, 1))  # e.g. [1]
        self.assertTrue(k_clique(self.g2, 2))  # e.g. [1, 5]
        self.assertTrue(k_clique(self.g2, 3))  # e.g. [2, 3, 5]
        self.assertFalse(k_clique(self.g2, 4))


if __name__ == '__main__':
    unittest.main()
