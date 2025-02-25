'''
Merge Two Sorted Linked List

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

SOLN: Similar to Merge Sort ARRAY
- node moves karna haii data nahi karna haii

APPROCH:
- Create Dummy Node
- Loop on Left and right and compare value

'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    ans = ListNode(-1)
    mptr = ans
    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            mptr.next = list1
            mptr = list1
            list1 = list.next
        else:
            # right wala xota haii
            mptr.next = list2
            mptr = list2
            list2 = list.next
    if list1 is not None:
        mptr.next = list1
        # mptr = list1
        # list1 = list1.next
    if list2 is not None:
        mptr.next = list2
        # mptr = list2
        # list2 = list2.next
    return ans.next
