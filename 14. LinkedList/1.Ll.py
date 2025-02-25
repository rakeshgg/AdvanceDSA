'''
Singly Linked List

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printLL(head):
    '''
    1. Print kardo data
    2. pointer ko aage le jaeo
    3. ruko jab pointer null ho
    '''
    temp = head
    while temp is not None:
        print(temp.data, end='-')
        temp = temp.next


first = Node(0)
second = Node(1)
third = Node(2)
fourth = Node(3)
fifth = Node(4)
first.next = second
second.next = third
third.next = fourth
fourth.next = fifth
printLL(first)
