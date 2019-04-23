import unittest

def decode(s):
    """Decode a string."""

    s_lst = list(s)

    frst = int(s_lst.pop(0))

    for item in s_lst:
        




class Test(unittest.TestCase):
    data = [
        ("0h", 'h'),
        ("2abh", 'h'),
        ("0h1ae2bcy", 'hey')
    ]

    def test_decode(self):
        for [s, expected] in self.data:
            result = decode(s)
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()