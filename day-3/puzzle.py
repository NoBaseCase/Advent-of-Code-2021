"""
--- Day 3: Binary Diagnostic ---
The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010

Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

--- Part Two ---
Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.

Both the oxygen generator rating and the CO2 scrubber rating are values that can be found in your diagnostic report - finding them is the tricky part. Both values are located using a similar process that involves filtering out values until only one remains. Before searching for either rating value, start with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers. Then:

Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
If you only have one number left, stop; this is the rating value for which you are searching.
Otherwise, repeat the process, considering the next bit to the right.
The bit criteria depends on which type of rating value you want to find:

To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
For example, to determine the oxygen generator rating value using the same example diagnostic report from above:

Start with all 12 numbers and consider only the first bit of each number. There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.
Then, consider the second bit of the 7 remaining numbers: there are more 0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second position: 10110, 10111, 10101, and 10000.
In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
In the fifth position, there are an equal number of 0 bits and 1 bits (one each). So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.
Then, to determine the CO2 scrubber rating value from the same example above:

Start again with all 12 numbers and consider only the first bit of each number. There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers with a 0 in the first position: 00100, 01111, 00111, 00010, and 01010.
Then, consider the second bit of the 5 remaining numbers: there are fewer 1 bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the second position: 01111 and 01010.
In the third position, there are an equal number of 0 bits and 1 bits (one each). So, to find the CO2 scrubber rating, keep the number with a 0 in that position: 01010.
As there is only one number left, stop; the CO2 scrubber rating is 01010, or 10 in decimal.
Finally, to find the life support rating, multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230.

Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. What is the life support rating of the submarine? (Be sure to represent your answer in decimal, not binary.)

"""

# reads file data and returns a array of characters


def read_data(filename):
    list = []
    with open(filename) as f:
        for line in f:
            # converts strings to integers
            list.append(line.replace("\n", ""))
    return list


def get_frequencies(data):
    # generates a template array initialized with zeros
    frequencies = []
    for i in range(len(data[0])):
        frequencies.append(0)

    # increments/decrements each index in the template array by 1 depending
    # if a one or zero is found, respectively.
    for line in data:
        for index in range(len(line)):
            if line[index] == "0":
                frequencies[index] -= 1
            else:
                frequencies[index] += 1
    return frequencies


# generates a string of 1's or 0's depending on the index value of the array given


def get_gamma_rate(data):
    gamma_rate = []
    for position in data:
        if position < 0:
            gamma_rate.append(0)
        elif position > 0:
            gamma_rate.append(1)
    return gamma_rate


# generates the inverse of the string that is passed in


def get_epsilon_rate(gamma_rate):
    epsilon_rate = []
    for item in gamma_rate:
        if item == 0:
            epsilon_rate.append(1)
        else:
            epsilon_rate.append(0)
    return epsilon_rate


# converts binary array into a decimal integer


def calculate_value(list):
    sum = 0
    for index in range(len(list)):
        if list[index] == 1:
            sum += 2 ** (len(list) - 1 - index)
    return sum


def power_consumption(data):
    frequencies = get_frequencies(data)
    gamma_rate = get_gamma_rate(frequencies)
    epsilon_rate = get_epsilon_rate(gamma_rate)
    gamma_value = calculate_value(gamma_rate)
    epsilon_value = calculate_value(epsilon_rate)

    print("|-----PART ONE------|")
    print("power consumption: {}  \n \n".format(gamma_value * epsilon_value))


data = read_data("input.txt")
power_consumption(data)


# Part two
def get_oxygen_generator_rating(data):
    # reassigned to a separate vaiable so that loop will not break
    output = data
    for index in range(len(data[0])):
        # temprorary arrays that will hold list of numbers that pertain to index position
        ones = []
        zeros = []
        # if there is only one item in our list, break the loop
        if len(output) == 1:
            break
        else:
            for item in output:
                # sorts numbers into two lists - those with ones and zeros
                if item[index] == "1":
                    ones.append(item)
                else:
                    zeros.append(item)
            # if the list with ones is greater or equal to the list with zeros, set that as our working list
            if len(ones) >= len(zeros):
                output = ones
            else:
                output = zeros
    # return the last remaining item in the list
    return output[0]


def get_c02_scrubber_rating(data):
    # reassigned to a separate vaiable so that loop will not break
    output = data
    for index in range(len(data[0])):
        # temprorary arrays that will hold list of numbers that pertain to index position
        ones = []
        zeros = []
        # if there is only one item in our list, break the loop
        if len(output) == 1:
            break
        else:
            # sorts numbers into two lists - those with ones and zeros
            for item in output:
                if item[index] == "1":
                    ones.append(item)
                else:
                    zeros.append(item)
            # if the list with zeros is less than or equal to the list with ones, set that as our working list
            if len(zeros) <= len(ones):
                output = zeros
            else:
                output = ones
    # return the last remaining item in the list
    return output[0]


# converts binary string to list of integers


def convert(binary_string):
    result = []
    for x in binary_string:
        result.append(int(x))
    return result


def life_support_rating(data):
    oxygen_generator_rating = get_oxygen_generator_rating(data)
    oxygen_generator_rating_value = convert(oxygen_generator_rating)
    oxygen_generator_rating_decimal_value = calculate_value(
        oxygen_generator_rating_value
    )

    c02_scrubber_rating = get_c02_scrubber_rating(data)
    c02_scrubber_rating_value = convert(c02_scrubber_rating)
    c02_scrubber_rating_decimal_value = calculate_value(c02_scrubber_rating_value)

    print("|-----PART TWO------|")
    print(
        "Oxygen generator Rating: {}\nOxygen generator Rating Value: {}\nDecimal Value: {}\n".format(
            oxygen_generator_rating,
            oxygen_generator_rating_value,
            oxygen_generator_rating_decimal_value,
        )
    )
    print(
        "C02 Scrubber Rating: {}\nC02 Scrubber Rating Value: {}\nDecimal Value: {}\n".format(
            c02_scrubber_rating,
            c02_scrubber_rating_value,
            c02_scrubber_rating_decimal_value,
        )
    )
    print(
        "Life Support Rating: {}".format(
            oxygen_generator_rating_decimal_value * c02_scrubber_rating_decimal_value
        )
    )


life_support_rating(data)
