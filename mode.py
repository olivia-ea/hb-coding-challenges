def mode(nums):
    """Find the most frequent num(s) in nums.

    >>> mode([1])
    {1}
    >>> mode([1, 2, 2, 2]) 
    {2}
    >>> mode([1, 1, 2, 2]) 
    {1, 2}
    """

    track_count = {}

    for num in nums:
        if num not in track_count:
            count = 1
            track_count[num] = count
        else:
            track_count[num] = count + 1

    max_val = max(track_count.values())
    mode = set([])

    for key, value in track_count.items():
        if value == max_val:
            mode.add(key)

    return mode

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()