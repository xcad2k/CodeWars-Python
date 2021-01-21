"""
This solution has a modified Node class for a shorter and cleaner solution
"""

class Node(object):
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt


def push(head, data):
    return Node(data, head)


def build_one_two_three():
    return push(push(push(None, 3), 2), 1)