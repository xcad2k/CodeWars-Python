#####################################################################################
#                                                                                   #
#   NAME:     Tribonacci Sequence                                                   #
#   RANK:     6kyu                                                                  #
#   URL:      https://www.codewars.com/kata/556deca17c58da83c00002db/train/python   #
#                                                                                   #
#####################################################################################

# works like fibonacci only with a base length of 3
def tribonacci(signature, n):
    while len(signature) < n:
        signature.append(signature[-1] + signature[-2] + signature[-3])
    return signature[:n]


print(tribonacci([0, 0, 1], 2))
