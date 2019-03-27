def rev_string(astring, i=0):
    """Return reverse of string using recursion.

    You may NOT use the reversed() function!

    Runtime: O(n)
    Space complexity: O(n)
    """
    new_str = list(astring)
    mid = len(new_str)//2 
    
    if i == mid:
        return ''.join(new_str)
    else:
        temp = new_str[i]
        new_str[i] = new_str[-1-i]
        new_str[-1-i] = temp
        i += 1
        return rev_string(new_str, i)

def rev_string_stack(astring):
    """
    Solve using stack. 
    """

    if astring == []:
        return
    else:
        return astring[-1] + rev_string_stack(astring[:-1])  

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()