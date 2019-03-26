def missing_number(lst, limit):
    """
    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8
    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8
    """
    lst = set(lst)

    compare = set()

    for i in range(1, limit):
        compare.add(i)
        i += 1    

    return compare.difference(lst)


if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()