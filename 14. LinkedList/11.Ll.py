'''
Add two Numbers using Linked List

-> 2->4->x
-> 2 -> 3 -> 4 -> x
two ways to come from right to left
- Using Recursion
- Reverse LL
  - Reverse both linked list
  - add
  - ans linked list reverse


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
        third = Node(3)
        fourth = Node(4)
        fifth = Node(0)
        sixth = Node(6)
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


def reverseLL(head):
    prev = None
    curr = head
    next = curr.next
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def addTwoLL(head1, head2):
    # step-1 reverse both linked list
    head1 = reverseLL(head1)
    head2 = reverseLL(head2)
    ansHead = None
    ansTail = None
    # step-2 add both linked list
    # step-2 reverse ans linked list
    carry = 0
    while head1 is not None and head2 is not None:
        # calculate sum
        sum = carry + head1.data + head2.data
        digit = sum % 10
        carry = sum//10
        newNode = Node(digit)
        # first node
        if ansHead is None:
            ansHead = newNode
            ansTail = newNode
        else:
            ansTail.next = newNode
            ansTail = newNode
        head1 = head1.next
        head2 = head2.next
    # if head1 length head2 se jyda haii
    while head1 is not None:
        sum = carry + head1.data
        digit = sum % 10
        carry = sum//10
        newNode = Node(digit)
        ansTail.next = newNode
        ansTail = newNode
        head1 = head1.next
    # if head2 length head1 se jyda haii
    while head2 is not None:
        sum = carry + head2.data
        digit = sum % 10
        carry = sum//10
        newNode = Node(digit)
        ansTail.next = newNode
        ansTail = newNode
        head2 = head2.next
    # carry avi baccha haii !.e Zero nahi hota
    while carry != 0:
        sum = carry
        digit = sum % 10
        carry = carry // 10
        newNode = Node(digit)
        ansTail.next = newNode
        ansTail = newNode
    ans = reverseLL(ansHead)
    # ans = ansHead
    return ans


obj1 = SLL()
obj1.create_ll()
obj1.printLL()

obj2 = SLL()
obj2.create_ll()
obj2.printLL()
ans = addTwoLL(obj1.head, obj2.head)
obj3 = SLL()
obj3.head = ans
obj3.printLL()
