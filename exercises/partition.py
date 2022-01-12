from nondeterminism import *


@nondeterministic
def partition(v: list):
    """
    Can we split the list into two distinct lists such that their sums are
    equal?

    :param v: The initial list.
    :return: True if there at least one partition. False otherwise.
    """
    n = len(v)
    success()
