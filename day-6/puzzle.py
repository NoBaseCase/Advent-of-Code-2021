def read_data(filename):
    with open(filename, "r") as file:
        first_line = file.readline()
    values = first_line.split(",")
    results = [int(i) for i in values]
    return results


def initialize_hashmap(hashmap, data):
    for i in range(9):
        hashmap.append(0)
    for i in range(len(data)):
        hashmap[data[i]] += 1
    return hashmap


def decrement_values(hashmap):
    first_value = hashmap[0]
    shift_list = hashmap[1:]
    if first_value > 0:
        shift_list[6] += first_value
    shift_list.append(first_value)
    return shift_list


def number_of_fish(hashmap):
    total = 0
    for fish in hashmap:
        total += fish
    return total


hashmap = []
data = read_data("input.txt")
number_of_days = 256
hashmap = initialize_hashmap(hashmap, data)
for i in range(number_of_days):
    hashmap = decrement_values(hashmap)
print("total number of fish: {}".format(number_of_fish(hashmap)))
