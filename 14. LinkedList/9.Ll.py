'''
Remove Duplicate From Sorted Linked List

Approch1: curr.data compare with curr.next.data
         1. if not equal than incremnt curr = curr.next
         2. If equal than curr.next = curr.next.next

Remove Duplicate from Unsorted Linked List
Approch1: use nested Loop - har node ke lie puri linked list traverse karoge
Approch2: use Maps to solve - store data:true/false
Approch3: Sort and use above Logic

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:

    def __init__(self):
        self.head = None
        self.tail = None

    def create_ll(self):
        first = Node(1)
        second = Node(2)
        third = Node(2)
        fourth = Node(2)
        fifth = Node(4)
        sixth = Node(4)
        # seven = Node(70)
        # eighth = Node(80)
        # ninth = Node(90)
        self.head = first
        first.next = second
        second.next = third
        third.next = fourth
        fourth.next = fifth
        fifth.next = sixth
        # sixth.next = seven
        # seven.next = eighth
        # eighth.next = ninth
        # ninth.next = None
        self.tail = sixth

    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end='->')
            temp = temp.next
        print("\n")

    def removeDuplicate(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        # single node
        if self.head.next is None:
            print("single node")
            return
        # > 1 Node
        curr = self.head
        # curr ko age wali node se compare
        while curr is not None:
            # can be None curr.next so check that
            if (curr.next) and (curr.data == curr.next.data):
                curr.next = curr.next.next
                # curr is not shifted to next node only link updated
                # node id auto delted in python if no pointer pointed to that Node
                # garbage collector
            else:
                curr = curr.next
                # curr is not shifted to next node


obj = SLL()
obj.create_ll()
obj.printLL()
obj.removeDuplicate()
obj.printLL()
