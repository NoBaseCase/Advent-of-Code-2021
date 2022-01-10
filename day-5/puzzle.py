class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# read in the input data
def read_data(filename):
    list = []
    with open(filename) as f:
        for line in f:
            # converts strings to integers
            list.append(line.replace("\n", ""))
    return list


# creates a list of coordinate pairs
def generate_coordinates(data):
    coordinate_list = []
    for item in data:
        split_list = item.split(" -> ")
        start_point = split_list[0].split(",")
        end_point = split_list[1].split(",")
        coodinate_container = []
        start_coordinate = Coordinate(int(start_point[0]), int(start_point[1]))
        end_coordinate = Coordinate(int(end_point[0]), int(end_point[1]))
        coodinate_container.append(start_coordinate)
        coodinate_container.append(end_coordinate)
        coordinate_list.append(coodinate_container)
    return coordinate_list


# creates an n x n grid
def generate_map(n):
    grid = []
    for i in range(n + 1):
        row = []
        for j in range(n + 1):
            row.append(0)
        grid.append(row)
    return grid


# finds the largest value in a list of coordinate pairs
def find_largest_value(coordinate_list):
    largest = 0
    for coordinate_set in coordinate_list:
        for coordinate in coordinate_set:
            if coordinate.x > largest:
                largest = coordinate.x
            elif coordinate.y > largest:
                largest = coordinate.y
    return largest


def draw_diagnal_line(grid, a, b):
    # select a starting point
    starting_coordinate = a
    # determines difference between two points i.e how many times to repeat
    difference = abs(a.x - b.x)
    # selects the starting point that is closest to the first index of our grid
    # because the incrementation is postive
    if b.y < a.y:
        starting_coordinate = b
    if positive_slope(a, b):
        for i in range(difference + 1):
            grid[starting_coordinate.y + i][starting_coordinate.x - i] += 1
    else:
        for i in range(difference + 1):
            grid[starting_coordinate.y + i][starting_coordinate.x + i] += 1
    return grid


def draw_verticle_line(grid, a, b):
    # determine the coordinate with the smallest y value
    smallest = min(a.y, b.y)
    # find the difference between the bigger and smaller y value
    y_difference = abs(a.y - b.y)
    # starting at the position of the coordiante with the smallest y value,
    # mark the grid, and then repeat the process with each row creating a verticle line.
    for i in range(y_difference + 1):
        grid[smallest + i][a.x] += 1
    return grid


def draw_horizontal_line(grid, a, b):
    # determine the coordinate with the smallest x value
    smallest = min(a.x, b.x)
    # find the difference between the bigger and smaller x value
    x_difference = abs(a.x - b.x)

    # starting at the position of the coordiante with the smallest x value,
    # mark the grid, and then repeat the process with each row creating a horizontal line.
    for i in range(x_difference + 1):
        grid[a.y][smallest + i] += 1
    return grid


# checks for a 45 degree angle between two give points
def has_45_degree_slope(x, y):
    if abs((y.y - x.y) / (x.x - y.x)) == 1:
        return True
    else:
        return False


# checks for a postive slope between two given points
def positive_slope(x, y):
    if ((y.y - x.y) / (x.x - y.x)) == 1:
        return True
    else:
        return False


def mark_grid(grid, coordinates):
    for coordinate_set in coordinates:
        # checks for verticle line
        if coordinate_set[0].x == coordinate_set[1].x:
            grid = draw_verticle_line(grid, coordinate_set[0], coordinate_set[1])
        # checks for horizontal line
        elif coordinate_set[0].y == coordinate_set[1].y:
            grid = draw_horizontal_line(grid, coordinate_set[0], coordinate_set[1])
        # checks for a 45 degree diagnal line
        elif has_45_degree_slope(coordinate_set[0], coordinate_set[1]):
            grid = draw_diagnal_line(grid, coordinate_set[0], coordinate_set[1])
    return grid


# calculates the overlap total score
def get_overlap_total(grid):
    output = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] >= 2:
                output += 1
    return output


data = read_data("input.txt")
coordinates = generate_coordinates(data)
largest_value = find_largest_value(coordinates)
grid = generate_map(largest_value)
marked_grid = mark_grid(grid, coordinates)
print("Part two | Total Score: {}".format(get_overlap_total(grid)))

# Note: to solve part one of the problem, comment out the last elif statement on the mark_grid() method


# PART
