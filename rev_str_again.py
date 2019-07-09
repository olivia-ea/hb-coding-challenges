def reverse_str():

    str_lst = list(str)

    iterations = len(str_lst)//2

    # if hello, 5//2 = 2

    i = 0
    while i < iterations:
        anchor = str_lst[i]
        str_lst[i] = str_lst[-1-i]
        str_lst[-1-i] = anchor
        i+=1

    return str_lst


"""
str = 'hello'

str_lst = ['h','e','l', 'l', 'o']

"""