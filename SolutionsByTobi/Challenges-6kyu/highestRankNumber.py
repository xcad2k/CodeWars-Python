#####################################################################################
#                                                                                   #
#   NAME:     Highest Rank Number in an Array                                       #
#   RANK:     6kyu                                                                  #
#   URL:      https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/train/python   #
#                                                                                   #
#####################################################################################


def highest_rank(arr):
    # This initializes a dictionary containing all values as keys in arr and a value of 0
    count = {a: 0 for a in set(arr)}
    for i in arr:
        count[i] += 1
    # This sorts by x[1] which is the count and as a second compare it by x[0] which is the number itself (this will be used if x[1] is the same on the objects). At the end I return the first property (the value) of the last element in the sorted list
    return sorted(count.items(), key=lambda x: (x[1], x[0]))[-1][0]


print(highest_rank([13, 36, 48, 33, 47, 22, 22, 27, 2, 6, 45, 3, 33, 49, 40, 18]))
