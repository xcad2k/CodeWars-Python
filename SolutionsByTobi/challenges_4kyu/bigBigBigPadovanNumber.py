#####################################################################################
#                                                                                   #
#   NAME:     Big Big Big Padovan Number                                            #
#   RANK:     4kyu                                                                  #
#   URL:      https://www.codewars.com/kata/5819f1c3c6ab1b2b28000624/train/python   #
#                                                                                   #
#####################################################################################

from math import comb, ceil


def padovan(n):
    n += 2
    return sum(comb(j, n - 2 * j) for j in range(ceil(n / 3), int(n / 2) + 1))


print(padovan(10000))
