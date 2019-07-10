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

    counter = 0

    flst1 = split_lst(lst1)
    flst2 = split_lst(lst2)

    for i in :
        abs(steps) = flst1[i][i] - flst2[i][i]
        counter += steps
    return counter





     
