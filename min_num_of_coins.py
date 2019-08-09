import unittest

def min_num_of_coins(coin_arr, target):

    


class Test(unittest.TestCase):
    data = [
        ([25, 10, 5, 1], 75, [25, 25, 25]), 
        ([25, 10, 5, 1], 51, [25, 25, 1])    
        ]

    def test_compress_string(self):
        for [coin_arr, target, expected] in self.data:
            result = min_num_of_coins(coin_arr, target)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()