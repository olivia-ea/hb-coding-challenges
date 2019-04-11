import unittest

def addition(x, y):
    """Add two integers together."""

    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        return ("Invalid type.")


class Test(unittest.TestCase):
    data = [
        (1, 1, 2), 
        ('a', 'b', "Invalid type.")
    ]

    def test_addition(self):
        """Test addition function."""

        for [test_x, test_y, expected] in self.data:
            result = addition(test_x, test_y)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

    # if not result.failed:
    #     print("ALL TESTS PASSED. GOOD WORK!")
    # print()