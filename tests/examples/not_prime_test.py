import unittest
from examples import not_prime


class TestNotPrime(unittest.TestCase):
    def test_prime_number(self):
        self.assertFalse(not_prime(2))
        self.assertFalse(not_prime(7))

    def test_not_prime_number(self):
        self.assertTrue(not_prime(6))
        self.assertTrue(not_prime(100))


if __name__ == '__main__':
    unittest.main()
