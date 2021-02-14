#####################################################################################
#                                                                                   #
#   NAME:     Your order, please                                                    #
#   RANK:     6kyu                                                                  #
#   URL:      https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python   #
#                                                                                   #
#####################################################################################

import re


def sortAlgo(e):
    # e stands for the word
    temp = re.findall(r'\d+', e)
    # return value is the key we're using in the sorting function
    return temp[0]


def order(sentence):
    if sentence == "":
        return sentence
    arr = sentence.split(" ")
    arr.sort(key=sortAlgo)
    return " ".join(arr)


print(order("is2 Thi1s T4est 3a"))
