def move_zeros(array):
    return sorted(array, key=lambda x: 1 if x == 0 and x is not False else 0)


print(move_zeros([9,False,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))