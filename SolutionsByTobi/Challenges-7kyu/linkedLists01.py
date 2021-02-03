#####################################################################################
#                                                                                   #
#   NAME:     Linked Lists - Push & BuildOneTwoThree                                #
#   RANK:     7kyu                                                                  #
#   URL:      https://www.codewars.com/kata/55be95786abade3c71000079/train/python   #
#                                                                                   #
#####################################################################################

"""
This solution doesn't change the Node class
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    result_node = Node(data)
    result_node.next = head
    return result_node


def build_one_two_three():
    head = Node(3)
    head = push(head, 2)
    head = push(head, 1)
    return head
