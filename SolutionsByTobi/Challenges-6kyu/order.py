#####################################################################################
#                                                                                   #
#   NAME:     Your order, please                                                    #
#   RANK:     6kyu                                                                  #
#   URL:      https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python   #
#                                                                                   #
#####################################################################################

import re


def order(sentence):
    if sentence == "": return ""
    result = sentence.split(' ')
    for word in sentence.split(' '):
        result[int(re.findall('\d+', word)[0]) - 1] = word
    return " ".join(result)


# same solution without regex
def order2(sentence):
    if sentence == "": return ""
    result = sentence.split(' ')
    for word in sentence.split(' '):
        result[int("".join([c for c in word if c.isdigit()])) - 1] = word
    return " ".join(result)


# One line solution... its based on the fact that numbers will be sorted before other chars
def order3(sentence):
    return ' '.join(sorted(sentence.split(), key=lambda w: sorted(w)))


print(order("4of Fo1r pe6ople g3ood th5e the2"))
print(order2("4of Fo1r pe6ople g3ood th5e the2"))
print(order3("4of Fo1r pe6ople g3ood th5e the2"))
