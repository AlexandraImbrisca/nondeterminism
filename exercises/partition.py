from nondeterminism import *


@nondeterministic
def partition(v: list):
    """
    Can we split the list into two distinct lists such that their sums are
    equal?

    :param v: The initial list.
    :return: True if there at least one partition. False otherwise.
    """
    sum1 = 0
    sum2 = 0

    for x in v:
        i = choice([1, 2])
        if i == 1:
            sum1 += x
        else:
            sum2 += x

    if sum1 == sum2:
        success()
    fail()
