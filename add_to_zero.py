import unittest

def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0."""

    set_nums = set(nums)

    for n in nums:
        if -n in set_nums:
            return True
      
    return False

class Test(unittest.TestCase):
    data = [
        ([], False),
        ([1], False),
        ([1, 2, 3], False), 
        ([1, 2, 3, -2], True),
        ([0, 1, 2], True)
    ]

    def test_add_to_zero(self):
        for [nums, expected] in self.data:
            result = add_to_zero(nums)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
