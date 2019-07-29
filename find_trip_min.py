# [1.01, 1.5, 2.5, 1.2, 1.01]

# 1.01 < weight < 3

# max = 3

# [1.01+1.5, 2.5, 1.2+1.01]

# output = 3

def find_trip_min(weight):

    num_of_trip = 0
    multiple_trip = []

    for bag in weight:
        if bag > 1.99:
            num_of_trip += 1
        else:
            multiple_trip.append(bag)


    for bag in multiple_trip:
        while len(multiple_trip) > 1:
            max_num = max(multiple_trip)
            min_num = min(multiple_trip)
            if max_num + min_num < 3:
                num_of_trip += 1
                multiple_trip.remove(max_num)
                multiple_trip.remove(min_num)
        else:
            num_of_trip += 1 
               
    return num_of_trip

    


