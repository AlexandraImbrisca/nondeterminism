import unittest
from exercises import n_queens


class TestNQueens(unittest.TestCase):
    def test_no_solution(self):
        self.assertFalse(n_queens(2))
        self.assertFalse(n_queens(3))

    def test_valid_solution(self):
        self.assertTrue(n_queens(1))  # e.g. [(0, 0)]
        self.assertTrue(n_queens(4))  # e.g. [(0, 1), (1, 3), (2, 0), (3, 2)]

        # This might take a while (at most n^3 possible solutions)
        # e.g. [(0, 0), (1, 4), (2, 7), (3, 5), (4, 2), (5, 6), (6, 1), (7, 3)]
        # self.assertTrue(n_queens(8))


if __name__ == '__main__':
    unittest.main()
