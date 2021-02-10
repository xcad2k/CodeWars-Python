#####################################################################################
#                                                                                   #
#   NAME:     Consonant Value                                                       #
#   RANK:     6kyu                                                                  #
#   URL:      https://www.codewars.com/kata/59c633e7dcc4053512000073/train/python   #
#                                                                                   #
#####################################################################################

import re


def solve(s):
    return max(map(lambda x: sum(ord(a) - ord('a') + 1 for a in x), re.split('[aeiou]', s)))