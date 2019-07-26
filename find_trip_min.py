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

    # multiple_trip.sort()

    


