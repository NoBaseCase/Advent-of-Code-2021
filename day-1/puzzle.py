"""
To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
In this example, there are 7 measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?

"""

# reads in data from input file
def read_data(filename):
    list = []
    with open(filename) as f:
        for line in f:
            # converts strings to integers
            list.append(int(line))
    return list


# returns the sum of instances where the nth item is greather than n-1
def larger_than_previous(list):
    sum = 0
    # start on the second element of the list (since we are comparing downwards)
    for i in range(1, len(list)):
        if list[i] > list[i - 1]:
            sum += 1
    return sum


# returns the sum of instances where a group of n items sum (n + n-1 + n-2) is greather than n-1 (n-1 + n-2 + n-3) sum
def three_measurement_sliding_window_sum(list):
    increased_sum = 0
    for index in range(3, len(list)):
        leading_sum = list[index] + list[index - 1] + list[index - 2]
        trailing_sum = list[index - 1] + list[index - 2] + list[index - 3]
        if leading_sum > trailing_sum:
            increased_sum += 1
    return increased_sum


number_list = read_integers("input.txt")
print(
    "sums are larger than the previous sum: {}".format(
        larger_than_previous(number_list)
    )
)
print(
    "Groups of sums larger than the previous: {}".format(
        three_measurement_sliding_window_sum(number_list)
    )
)
