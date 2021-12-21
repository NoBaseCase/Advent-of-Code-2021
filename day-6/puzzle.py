def read_data(filename):
    with open(filename, "r") as file:
        first_line = file.readline()
    values = first_line.split(',')
    results = [int(i) for i in values]
    return results

def decrement_values(data):
    new_fish = []
    for i in range(len(data)):
        if data[i] == 0:
            data[i] = 6
            new_fish.append(8)
        else:
            data[i] -= 1
    for fish in new_fish:
        data.append(fish)
    return data

data = read_data('input.txt')
number_of_days = 256
for i in range(1, number_of_days + 1):
    data = decrement_values(data)
    print('After {} days, there are: {} lantern fish'.format(i, len(data)))
    