from nondeterminism import *


@nondeterministic
def q_sums(v: list, q: int):
    """
    Is there a subset whose sum of all the elements equals q?

    :param v: The initial set of elements.
    :param q: The desired sum.
    :return: True if we can find a subset that satisfies the condition.
    False otherwise.
    """
    n = len(v)
    success()
