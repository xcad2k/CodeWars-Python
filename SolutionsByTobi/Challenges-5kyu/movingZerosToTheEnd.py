def move_zeros(array):
    return sorted(array, key=lambda x: 1 if x == 0 and not x is False else 0)
