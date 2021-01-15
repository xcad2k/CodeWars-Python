def multiplication_table(size):
    return [[x * y for y in range(1, size + 1)] for x in range(1, size + 1)]

print(multiplication_table(3))