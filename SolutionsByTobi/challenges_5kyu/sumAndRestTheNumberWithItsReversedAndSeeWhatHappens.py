################################################################################
#                                                                              #
#   NAME:     Sum and Rest the Number with its Reversed and See What Happens   #
#   RANK:     5kyu                                                             #
#   URL:      https://www.codewars.com/kata/5603a9585480c94bd5000073           #
#                                                                              #
################################################################################

"""
DISCLAIMER:
PRETTY BAD PERFORMING BUT WORKING
BETTER SOLUTION CAN BE FOND IN sumAndRestTheNumberWithItsReversedAndSeeWhatHappens02.py
"""


def sum_dif_rev(n):
    i, j = 44, 0
    while True:
        i += 1
        invers = int(str(i)[::-1])
        if str(i)[-1] != '0' and invers != i and (invers + i) % abs(invers - i) == 0:
            j += 1
        if j == n:
            return i


print(sum_dif_rev(65))
