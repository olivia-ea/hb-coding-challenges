import unittest

def max_of_three(num1, num2, num3):
    
    """Returns the largest of three integers"""

    nums = [num1, num2, num3]

    max_num = num1
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num



class Test(unittest.TestCase):
    data = [([1, 2, 3], 3),
            ([1, 2, 1], 2)
    ]

    def test_max_of_three(self):
        for [nums, expected] in self.data:
            result = max_of_three(nums)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
