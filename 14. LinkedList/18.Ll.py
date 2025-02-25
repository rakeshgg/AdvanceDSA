'''
Rotate List
61. Rotate List
Given the head of a linked list, rotate the list to the right by k places.
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

K % len == 0, Not required to rotate
K % len -> actual rotate k - value
using that do actual rotation

let k = 2 than isolate last two and add in front


'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getlength(temp):
    len = 0
    while temp:
        len += 1
        temp = temp.next
    return len


def rotateRight(head, k):
    if head is None:
        return head
    len = getlength(head)
    actualRotateK = k % len
    # no rotation requireed
    if actualRotateK == 0:
        return head
    newLastNodePos = len - actualRotateK - 1
    newHead = None
    newLastNode = head
    for i in range(newLastNodePos):
        newLastNode = newLastNode.next
    newHead = newLastNode.next
    newLastNode.next = None
    it = newHead
    while it is not None:
        it = it.next
    it.next = head
    return newHead
