# [(123, 244)] [(321, 435)]

# 2+2+2+1+1 = 8

def get_last_digit(num):
    """Helper function."""

    return num % 10

def split_nums(num):
    """Valid for 3 digit numbers."""

    split_lst = []
    itr = 3

    while itr > 0:
        split_num = get_last_digit(num)
        num = num // 10
        split_lst.insert(0, split_num)
        itr -= 1
    return split_lst

def split_lst(lst):
    """Split individual lists."""

    combine_split_lst = []

    i = 0
    for num in lst[i]:
        split_lst = split_nums(num)
        combine_split_lst.append(split_lst)
    return combine_split_lst

def count_steps(lst1, lst2):

    flst1 = split_lst(lst1)
    flst2 = split_lst(lst2)

    counter = 0
    i = 0

    for item in lst1, lst2:
        print(item)
        steps = abs(flst1[i] - flst2[i])
        counter += steps
        i += 1
    return counter


[i - j for i, j in zip(a, b)]

"""
Alternatively, it is possible to cast the integer as a str  to split and then back to integers.

lst = list(int(digit) for digit in str(12345)) //list comprehension

OR

lst = []
num = 12345
for digit in str(num):
    lst.append(int(digit))

"""





     
