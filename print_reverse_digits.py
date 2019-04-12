import unittest


def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place."""

    while num:
        next_digit = num % 10
        print(next_digit)
        num = (num - next_digit) // 10


class Test(unittest.TestCase):
    data = [
        (1, 1),
        (314, 413),
        (12, 21)
    ]

    def test_primes(self):
        for [nums, expected] in self.data:
            result = print_digits(nums)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()