import unittest



def find_mode(nums):
    """Find the most frequent num(s) in nums."""

    count_dict = {}
    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1
    return max(count_dict, key=count_dict.get)


class Test(unittest.TestCase):
    data = [([1, 2, 3, 4, 4], 4),
            ([5, 0, 1, 0], 0),
            ([1], 1)
    ]

    def test_find_mode(self):
        for [nums, expected] in self.data:
            result = find_mode(nums)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
