import unittest


def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    """

    stack = []

    opening_pairs = {'(', '{', '[', '<'}

    closing_pairs = {')', '}', ']', '>'}

    for item in phrase:
        if item in opening_pairs:
            stack.append(item)
        if item in closing_pairs:
            stack.pop()

    if stack == []:
        return True
    return False


class Test(unittest.TestCase):
    data = [
        ("<ok>", True),
        ("<[ok]>", True),
        ("<[{(yay)}]>", True), 
        ("No brackets here!", True),
        # ("<{Not Ok>}", False),
        # (">", False),
        # ("(This has {too many} ) closers. )", False),
        # ("(Oops!){", False),
        # ("{[[This has too many open square brackets.]}", False)
    ]

    def test_has_balanced_brackets(self):
        for [phrase, expected] in self.data:
            result = has_balanced_brackets(phrase)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()



"""
Possible solutions:
1. Push opening parens in stack and pop on closing parens

"""








