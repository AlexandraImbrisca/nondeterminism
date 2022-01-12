from nondeterminism import *


@nondeterministic
def composite(n):
    d = choice(range(2, n))
    if n % d == 0:
        success()
    else:
        fail()


def prime(n):
    if n < 2:
        return False
    else:
        return not composite(n)


if __name__ == '__main__':
    numbers = [6]
    for n in numbers:
        if prime(n):
            print('The integer', n, 'is prime')
        else:
            print('The integer', n, 'is not prime')
