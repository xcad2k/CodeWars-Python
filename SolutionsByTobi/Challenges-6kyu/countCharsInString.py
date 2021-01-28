"""
CODEWARS CHALLENGE: Count characters in your string
URL: https://www.codewars.com/kata/52efefcbcdf57161d4000091
"""


def count(str):
    result = {}
    for char in str:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


print(count("abdlskdaa"))