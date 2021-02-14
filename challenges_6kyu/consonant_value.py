#####################################################################################
#                                                                                   #
#   NAME:     Consonant value                                                       #
#   RANK:     6kyu                                                                  #
#   URL:      https://www.codewars.com/kata/59c633e7dcc4053512000073/python         #
#                                                                                   #
#####################################################################################

import re


# Solution 1
def solve(s):
    return max(
        map(
            lambda string:
                sum(
                    ord(char) - 96
                    for char in string
                ),
            re.split('[aeiou]', s)
        )
    )


# Tests
print(solve("chruschtschov"))
