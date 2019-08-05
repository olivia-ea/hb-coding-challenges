import unittest

def get_max_profit(stock_prices):

    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices.')
    
    min_price  = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

 
    for current_time in range(1, len(stock_prices)):
        current_price = stock_prices[current_time]

        potential_profit = current_price - min_price

        max_profit = max(max_profit, potential_profit)

        min_price  = min(min_price, current_price)

    return max_profit
    

class Test(unittest.TestCase):
    data = [
        ([10, 7, 5, 8, 11, 9], 6)
    ]

    def test_compress_string(self):
        for [stock_prices, expected] in self.data:
            result = get_max_profit(stock_prices)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
