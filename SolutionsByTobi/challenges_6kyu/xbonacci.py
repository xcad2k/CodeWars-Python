#####################################################################################
#                                                                                   #
#   NAME:     Fibonacci, Tribonacci and friends                                     #
#   RANK:     6kyu                                                                  #
#   URL:      https://www.codewars.com/kata/556e0fccc392c527f20000c5/train/python   #
#                                                                                   #
#####################################################################################

def xbonacci(signature, n):
    length = len(signature)
    while len(signature) < n:
        signature.append(sum(signature[-length:]))
    return signature[:n]
