import unittest

def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """

    def _recursive_index(needle, haystack, count):
        """Helper function."""

        if count == len(haystack):
            return None

        if haystack[count] == needle:
            print(count)
        recursive_index(needle, haystack, count + 1) 

    return _recursive_index(needle, haystack, 0)

class Test(unittest.TestCase):
    data = [
        ("hey", ["hey", "there", "you"], 0),
        ("you", ["hey", "there", "you"], 2),
        ("porcupine", ["hey", "there", "you"], None)
    ]

    def test_recursive_index(self):
        for [needle, haystack, expected] in self.data:
            result = recursive_index(needle, haystack)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

