def multiplication_table(size):
    return [[x + y - 1 if x == 1 or y == 1 else x * y for y in range(1, size + 1)] for x in range(1, size + 1)]