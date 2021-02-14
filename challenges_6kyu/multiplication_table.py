#####################################################################################
#                                                                                   #
#   NAME:     Multiplication table                                                  #
#   RANK:     6kyu                                                                  #
#   URL:      https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python   #
#                                                                                   #
#####################################################################################

# Solution 1
def multiplication_table(size):

    table = []

    for x in range(1, size + 1):
        yTable = []
        for y in range(1, size + 1):
            yTable.append(y*x)
        table.append(yTable)

    return table


# Solution 2
def multiplication_table2(size):
    return [[y * x for y in range(1, size + 1)] for x in range(1, size + 1)]


# Tests
print(multiplication_table(3))
print(multiplication_table2(3))
