class Tile:
    def __init__(self, value):
        self.value = value
        self.marked = False

# read in the input data
def read_data(filename):
    list = []
    with open(filename) as f:
        for line in f:
            # converts strings to integers
            list.append(line.replace("\n", ""))
    return list

# coverts a list of strings into a list of integers
def get_drawn_numbers(list):
    output = []
    list = list.split(',')
    for item in list:
        output.append(int(item))
    return output

# takes a 2-D array (list of numbers) and creates n/5 5x5 bingo board        
def generate_bingo_boards(data):
    # remove the first two elements in the data set
    data = data[2:]

    # create new data set object to contain
    formatted_data = []
    for item in data:
        if not item:
            continue
        else:
            formatted_data.append(item.split())

    # convert strings into tile objects
    for item in formatted_data:
        for i in range(len(item)):
            tile = Tile(int(item[i]))
            item[i] = tile

    # build the bingo board set list
    iterator = 0
    boardlist = []
    while(iterator < len(formatted_data)):
        board = []
        for x in range(iterator, iterator+5):
            board.append(formatted_data[x])
            iterator += 1
        boardlist.append(board)
    return boardlist

# makes all tiles that contain a given number
def mark_bingo_card(bingo_card, number):
    for row in bingo_card:
        for col in row:
            if col.value == number:
                col.marked = True
    return bingo_card

# checks wether a bingo card is a winner
def is_winner(bingo_card):
    # iterates through each row checking to see if every tile is marked
    for row in range(0, len(bingo_card)):
        flag = True
        for column in range(0, len(bingo_card[0])):
            # if any tile in the row is marked, break and continue
            if bingo_card[row][column].marked == False:
                flag = False
                break
        # if all tiles are set as marked
        if flag:
            return True

    # iterates through each column checking to see if every tile is marked
    for row in range(0, len(bingo_card)):
        flag = True
        # if any tile in the column is marked, break and continue
        for column in range(0, len(bingo_card[0])):
            if bingo_card[column][row].marked == False:
                flag = False
                break
        # if all tiles are set as marked
        if flag:
            return True

    return False

# returns the winning board and the number of the wining bingo card
def find_winning_board_set(drawn_numbers, bingo_boards):
    winning_set = []
    for number in drawn_numbers:
        for board in bingo_boards:
            board = mark_bingo_card(board, number)
            if is_winner(board):
                winning_set.append(board)
                winning_set.append(number)
                return winning_set
    return winning_set


def calculate_score(winning_board_set):
    score_sum = 0
    multiplier = winning_board_set[1]
    # adds the sum of all unmarked tile's value
    for row in winning_board_set[0]:
        for col in row:
            if col.marked == False:
                score_sum += col.value 
    return score_sum * multiplier

# finds the last winning board
def find_last_winning_board_set(drawn_numbers, bingo_boards):

    # temporary variables
    winning_board = []
    winning_number= 0
    winning_set = []

    # for every number drawn
    for x in range(len(drawn_numbers)):
        # for every bingo card available
        for i in range(len(bingo_boards)-1, 0, -1):
            # mark off the current bingo card (if it contains the number drawn)
            bingo_boards[i] = mark_bingo_card(bingo_boards[i], drawn_numbers[x])
            # check to see if the bingo car dis a winner - if it is, save the current board, and winning number
            # then remove the bingo board from the list of available boards
            if is_winner(bingo_boards[i]):
                winning_board = bingo_boards[i]
                winning_number= drawn_numbers[x]
                bingo_boards.pop(i)

    # append the winning board and numbe to a set and return
    winning_set.append(winning_board)
    winning_set.append(winning_number)
    return winning_set

# PART ONE
data = read_data('input.txt')
drawn_numbers = get_drawn_numbers(data[0])
boards = generate_bingo_boards(data)
winning_set = find_winning_board_set(drawn_numbers, boards)
score = calculate_score(winning_set)
print('The winning board score is: {}'.format(score))

# PART TWO
data = read_data('input.txt')
drawn_numbers = get_drawn_numbers(data[0])
boards = generate_bingo_boards(data)
winning_set = find_last_winning_board_set(drawn_numbers, boards)
score = calculate_score(winning_set)
print('|------PART TWO --------|')
print('The winning board score is: {}'.format(score))
        



