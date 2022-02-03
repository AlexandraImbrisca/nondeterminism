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
    sum = 0
    n = len(v)
    subset = []

    for _ in range(n):
        x = choice(v)
        if x in subset:
            fail()

        sum += x
        subset.append(x)

        if sum == q:
            success()
    fail()
