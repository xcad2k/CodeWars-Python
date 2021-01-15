def multiplication_table(size):

    table = []

    for x in range(1, size + 1):
        yTable = []
        for y in range(1, size + 1):
            yTable.append(y*x)
        table.append(yTable)

    return table


print(multiplication_table(3))
