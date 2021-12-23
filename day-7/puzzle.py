def read_data(filename):
    with open(filename, "r") as file:
        first_line = file.readline()
    values = first_line.split(',')
    results = [int(i) for i in values]
    return results

def smallest_fuel_cost(positions):
    fuel_cost = []
    for i in range(len(positions)):
        sum = 0
        position = positions[i]
        for j in range(len(positions)):
            sum = sum + abs(positions[j] - position)
        fuel_cost.append(sum)
    
    smallest = fuel_cost[0]
    for i in range(len(fuel_cost)):
        if fuel_cost[i] < smallest:
            smallest = fuel_cost[i]
    return smallest

def get_largest_value(list):
    largest = list[0]
    for i in range(1, len(list)):
        if list[i] > largest:
            largest = list[i]
    return largest+1

def get_sum(x): 
    sum = 0
    for i in range(1, x+1):
        sum += i
    return sum

def generate_fuel_mapping(x):
    dictionary = {}
    for i in range(x+1):
        value = get_sum(i)
        dictionary[i] = value
    return dictionary

def actual_fuel_cost(positions):
    fuel_cost = []
    largest = get_largest_value(positions)
    fuel_dictionary = generate_fuel_mapping(largest)
    # print(fuel_dictionary)
    for target in range(0, largest):
        total_fuel_cost = 0
        for j in range(len(positions)):
            difference  = abs(target - positions[j])
            fuel = fuel_dictionary[difference]
            total_fuel_cost += fuel
        fuel_cost.append(total_fuel_cost)
    smallest = fuel_cost[0]
    for i in range(len(fuel_cost)):
        if fuel_cost[i] < smallest:
            smallest = fuel_cost[i]
    return smallest

positions = read_data('input.txt')
largest = sum(positions)
print(largest)
# Part One
print('Part one: smallest fuel cost: {}'.format(smallest_fuel_cost(positions)))

# Part Two
print('Parat two: smallest fuel cost: {}'.format(actual_fuel_cost(positions)))


departments = 'airport, buildilng maintenence'