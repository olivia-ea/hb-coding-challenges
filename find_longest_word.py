"""
Write a function, find_longest_word, that takes a list of words and returns the 
length of the longest one.

"""

import unittest

def find_longest_word(words):

    max_len = len(words[0])

    for word in words:
        if len(word) > max_len:
            max_len = len(word)

    return max_len


class Test(unittest.TestCase):
    data = [(['hello', 'hi', 'hey'], 5),
            (['boy', 'girl'], 4)
    ]

    def test_find_longest_word(self):
        for [strs, expected] in self.data:
            result = find_longest_word(strs)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
