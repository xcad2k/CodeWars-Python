#####################################################################################
#                                                                                   #
#   NAME:     Fibonacci, Tribonacci and friends                                     #
#   RANK:     6kyu                                                                  #
#   URL:      https://www.codewars.com/kata/556e0fccc392c527f20000c5/train/python   #
#                                                                                   #
#####################################################################################

def xbonacci(signature, n):

    numElements = len(signature)

    for i in range(n):
        signature.append(
            sum(signature[-numElements:])
        )

    return signature[:n]


print(xbonacci([0, 0, 1, 1], 10))
