import unittest
from helpers import Graph
from exercises import vertex_cover


class TestVertexCover(unittest.TestCase):
    def setUp(self):
        self.g1 = Graph([1, 2, 3], [(1, 2), (1, 3), (2, 3)])
        self.g2 = Graph([1, 2, 3, 4, 5],
                        [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (3, 5),
                         (4, 5)])

    def test_small_graph(self):
        self.assertFalse(vertex_cover(self.g1, 1))
        self.assertTrue(vertex_cover(self.g1, 2))  # e.g. S = [1, 3]

    def test_bigger_graph(self):
        self.assertFalse(vertex_cover(self.g2, 1))
        self.assertFalse(vertex_cover(self.g2, 2))
        self.assertTrue(vertex_cover(self.g2, 3))  # e.g. S = [1, 3, 5]


if __name__ == '__main__':
    unittest.main()
