import unittest

def is_prime(num):

    if isinstance(num, int):
        if num < 2:
            return False
        elif num == 2:
            return True
        elif num % 2 == 0:
            return False


def primes(count):
    """Return count number of prime numbers, starting at 2.

    A prime number is a number >= 2 that is only evenly 
    divisible by itself and 1.
    """
    prime_nums = []
    num = 2

    if isinstance(count, int):
        while count > 0:
            if is_prime(num):
                prime_nums.append(num)
                count -= 1
            num += 1
        return prime_nums
    else:
        return ('Not a valid type or out of range.')



class Test(unittest.TestCase):
    data = [
        (1, [2]),
        (5, [2, 3, 5, 7, 11]),
        ('a', 'Not a valid type or out of range.')
    ]

    def test_primes(self):
        for [count, expected] in self.data:
            result = primes(count)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()