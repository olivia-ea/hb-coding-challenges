import unittest

def find_count(max_num, array):

    return array.count(max_num)

def freq_of_max(price):

    num_freq = []

    while price:
        for num in price:
            max_num = max(price)
            count = find_count(max_num, price)
            num_freq.append(count)
            price.pop(0)

    return num_freq


class Test(unittest.TestCase):
    data = [([5, 4, 5, 3, 2], [2, 1, 1, 1, 1])
    ]

    def test_max_of_three(self):
        for [price, expected] in self.data:
            result = freq_of_max(price)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
