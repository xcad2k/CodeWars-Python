#####################################################################################
#                                                                                   #
#   NAME:     Count characters in your string                                       #
#   RANK:     6kyu                                                                  #
#   URL:      https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python   #
#                                                                                   #
#####################################################################################


def count(str):
    result = {}
    for char in str:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


print(count("abdlskdaa"))