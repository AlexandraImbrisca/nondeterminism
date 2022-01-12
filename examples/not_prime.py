from nondeterminism import *
from math import floor, sqrt


@nondeterministic
def not_prime(n: int):
    i = choice(range(2, floor(sqrt(n)) + 1))
    if n % i == 0:
        success()
    fail()
