from nondeterminism import *


@nondeterministic
def n_queens(n: int):
    """
    Can we place n queens on a board of size nxn such that no queen attacks the
    others?

    :param n: The number of queens/the board dimension.
    :return: True if it's possible. False otherwise
    """
    success()
