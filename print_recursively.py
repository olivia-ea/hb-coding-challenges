import unittest


def print_recursively(lst):
    """Print items in the list, using recursion."""

    if lst:
        print(lst[0])
        print_recursively(lst[1:])

class Test(unittest.TestCase):
    data = [
        ([1, 2, 3], 123)
    ]

    def test_primes(self):
        for [nums, expected] in self.data:
            result = print_recursively(nums)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()