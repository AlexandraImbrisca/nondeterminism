from nondeterminism import *


@nondeterministic
def linear_search(v: list, e: int):
    n = len(v)
    if n <= 0:
        fail()

    i = choice(range(n))
    if v[i] == e:
        success()

    fail()
