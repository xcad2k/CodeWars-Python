#####################################################################################
#                                                                                   #
#   NAME:     Moving Zeros To The End                                               #
#   RANK:     5kyu                                                                  #
#   URL:      https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python   #
#                                                                                   #
#####################################################################################

def move_zeros(array):
    return sorted(array, key=lambda x: 1 if x == 0 and not x is False else 0)

def move_zeros2(array):
    return [x for x in array if x != 0 or x is False] + [x for x in array if x == 0 and x is not False]
