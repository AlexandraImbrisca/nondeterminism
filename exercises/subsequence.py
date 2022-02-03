from nondeterminism import *


@nondeterministic
def subsequence(v: list, k: int):
    """
    Can we find a subsequence of more than k equal values?

    :param v: The list of values.
    :param k: The minimum size of the subsequence.
    :return: True if at least one subsequence is available. False otherwise.
    """
    n = len(v)
    i = choice(range(n))
    j = choice(range(n))

    if j - i + 1 <= k:
        fail()

    for idx in range(i, j + 1):
        if v[idx] != v[i]:
            fail()

    success()
