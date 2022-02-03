from nondeterminism import *


@nondeterministic
def n_queens(n: int):
    """
    Can we place n queens on a board of size nxn such that no queen attacks the
    others?

    :param n: The number of queens/the board dimension.
    :return: True if it's possible. False otherwise
    """
    positions = []

    for idx in range(n):
        i = choice(range(n))
        j = choice(range(n))

        for (row, col) in positions:
            if row == i or col == j or row - col == i - j or row + col == i + j:
                fail()

        positions.append((i, j))

    success()
