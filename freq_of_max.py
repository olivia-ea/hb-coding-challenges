# price = [5, 4, 5, 2, 1]
# query = [1, 2, 3, 4, 5]

# output = [2, 1, 1, 1, 1]

def find_count(max_num, array):

    return array.count(max_num)

def freq_of_max(price):

    num_freq = []

    while price:
        for num in price:
            max_num = max(price)
            count = find_count(max_num, price)
            num_freq.append(count)
            price.pop(0)

    return num_freq


# redo problem with solution that doesn't modify array 

