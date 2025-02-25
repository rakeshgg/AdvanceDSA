'''
https://leetcode.com/problems/intersection-of-two-linked-lists/
Given the heads of two singly linked-lists headA and headB, return the
node at which the two lists intersect. If the two linked lists have no
intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no
intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected
node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are
different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B
(3rd node in A and 4th node in B) point to the same location in memory.

SOLN:
- Traverse both till one become NULL
  b is NUll than ovioulsy len(a) > len(b)
  so find length diff between these two
- Traverse in 2nd pass and initialize shorter one at diff
- if length same - Both Null no diff in length so start and compare

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    a = headA
    b = headB
    while a.next is not None and b.next is not None:
        if a is b:
            return a
        a = a.next
        b = b.next
    if a.next is None and b.next is None and a is not b:
        # both same position tail no intersection
        return 0
    if a.next is None:
        # b is greater
        # we need to find how much bigger it is
        blen = 0
        while b.next is not None:
            blen += 1
            b = b.next
        while blen:
            headB = headB.next
            blen -= 1
    else:
        # a is greater
        # we need to find how much bigger it is
        alen = 0
        while a.next is not None:
            alen += 1
            a = a.next
        while alen:
            headA = headA.next
            alen -= 1
    while headA is not headB:
        headA = headA.next
        headB = headB.next
    return headA
