def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.

    >>> has_balanced_brackets("<ok>")
    True
    >>> has_balanced_brackets("<[ok]>")
    True
    >>> has_balanced_brackets("<[{(yay)}]>")
    True
    >>> has_balanced_brackets("No brackets here!")
    True
    >>> has_balanced_brackets("<{Not Ok>}")
    False
    >>> has_balanced_brackets(">")
    False
    >>> has_balanced_brackets("(This has {too many} ) closers. )")
    False
    >>> has_balanced_brackets("(Oops!){")
    False
    >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
    False
    """

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()