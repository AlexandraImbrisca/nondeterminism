from nondeterminism import *


@nondeterministic
def sort(v: list):
    for x in v:
        if x <= 0:
            fail()

    n = len(v)
    aux = [0 for _ in v]

    for i in range(n):
        j = choice(range(n))
        if aux[j] > 0:
            fail()
        aux[j] = v[i]

    for i in range(n - 1):
        if aux[i] > aux[i + 1]:
            fail()

    print("Sorted array: %s" % aux)
    success()
