import unittest

def convert_coins(coin_count):

    coin_str = []

    for coin, quantity in coin_count.items():
        if quantity == 1:
            coin_str.append(str(quantity) + " " + str(coin)  + " " + "cent")
        else:
            coin_str.append(str(quantity) + " " + str(coin) + " " + "cents")

    return " ".join(coin_str)

def min_num_of_coins(coin_arr, target):

    coin_count = {}

    sorted(coin_arr, reverse=True)

    i = 0
    while target:
        while target >= coin_arr[i]:
            target = target - coin_arr[i]
            coin_count[coin_arr[i]] = coin_count.get(coin_arr[i], 0) + 1
        i += 1

    result_coins = convert_coins(coin_count)

    return result_coins

class Test(unittest.TestCase):
    data = [
        ([25, 10, 5, 1], 75, "3 25 cents"), 
        ([50, 10, 5, 1], 51, "1 50 cent and 1 1 cent")    
        ]

    def test_compress_string(self):
        for [coin_arr, target, expected] in self.data:
            result = min_num_of_coins(coin_arr, target)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()