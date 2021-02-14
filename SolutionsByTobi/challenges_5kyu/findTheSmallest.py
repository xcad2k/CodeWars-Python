#####################################################################################
#                                                                                   #
#   NAME:     Find the smallest                                                     #
#   RANK:     5kyu                                                                  #
#   URL:      https://www.codewars.com/kata/573992c724fc289553000e95/train/python   #
#                                                                                   #
#####################################################################################

def smallest(n):
    index, digit, insert_index = 0, 0, 0
    lowest = n * 10
    n_as_str = str(n)
    for i, char in enumerate(n_as_str):
        subst = n_as_str[:i] + n_as_str[i + 1:]
        for j in range(len(subst)):
            pass
    return [lowest, index, insert_index]


smallest(12345)
