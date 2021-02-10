#####################################################################################
#                                                                                   #
#   NAME:     Moving Zeros To The End                                               #
#   RANK:     5kyu                                                                  #
#   URL:      https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python   #
#                                                                                   #
#####################################################################################


# Solution 1
def move_zeros(array):
    return sorted(array, key=lambda x: True if x == 0 and x is not False else False)


# Tests
print(move_zeros([9,False,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))