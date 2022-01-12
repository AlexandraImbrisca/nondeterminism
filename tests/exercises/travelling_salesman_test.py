import unittest
from helpers import Graph
from exercises import travelling_salesman


class TestTravellingSalesman(unittest.TestCase):
    def setUp(self):
        self.g1 = Graph([1, 2, 3], [(1, 2)])
        self.g2 = Graph([1, 2, 3, 4], [(1, 2), (1, 4), (2, 3), (3, 4)])
        self.g3 = Graph([1, 2, 3, 4],
                        [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])

    def test_no_solution(self):
        self.assertFalse(travelling_salesman(self.g1))

    def test_valid_solution(self):
        self.assertTrue(travelling_salesman(self.g2))  # e.g. 1->2->3->4->1
        self.assertTrue(travelling_salesman(self.g3))  # e.g. 1->2->4->3->1


if __name__ == '__main__':
    unittest.main()
