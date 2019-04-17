import unittest

def calc(s):
    """Evaluate expressio using polish notation calculator."""

    tokens = s.split()

    


class Test(unittest.TestCase):
    data = [
        ("+ 1 2", 3),
        ("* 2 + 1 2", 6),
        ("+ 9 * 2 3", 15), 
        ("/ 6 - 4 2", 3),
        ("- 9 * 2 3", 3)
    ]

    def test_calc(self):
        for [s, expected] in self.data:
            result = calc(s)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
