#####################################################################################
#                                                                                   #
#   NAME:     Linked Lists - Push & BuildOneTwoThree                                #
#   RANK:     7kyu                                                                  #
#   URL:      https://www.codewars.com/kata/55be95786abade3c71000079/train/python   #
#                                                                                   #
#####################################################################################

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    if head is None:
        return Node(data)
    returnObj = Node(data)
    returnObj.next = head
    return returnObj


def build_one_two_three():
    chained = None
    chained = push(chained, 3)
    chained = push(chained, 2)
    chained = push(chained, 1)
    return chained
