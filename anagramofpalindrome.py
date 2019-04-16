import unittest

def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    letter_dict = {}
    # create empty dict to keep track of all unique letters

    for letter in word:
        letter_dict[letter] = letter_dict.get(letter, 0) + 1

    seen = False

    for count in letter_dict.values():
        if count % 2 != 0:  # look at all letter values that are odd
            if seen:    # only executes if TRUE; seen default is FALSE
                return False    
            seen = True
    return True

class Test(unittest.TestCase):
    data = [
        ("a", True),
        ("ab", False),
        ("aab", True), 
        ("arceace", True),
        ("arceaceb", False)
    ]

    def test_is_anagram_of_palindrome(self):
        for [word, expected] in self.data:
            result = is_anagram_of_palindrome(word)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()