# [(123, 244)] [(321, 435)]

# 2+2+2+1+1 = 8

def get_last_digit(num):
    """Helper function"""

    return num % 10

def split_nums(num):
    """Valid for 3 digit numbers"""

    itr = 3

    while itr > 0:
        split_num = get_last_digit(num)
        num = num // 10
        print(split_num)
        itr -= 1

def count_steps():
    pass 
