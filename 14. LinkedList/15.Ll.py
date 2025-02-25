'''
Merge Sort In Linked List

148. Sort List
Given the head of a linked list, return the list after sorting it in ascending order.
Input: head = [4,2,1,3]
Output: [1,2,3,4]
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Approch:
1. find mid
2. using mid divie array
3. RE divide
4. Merge

'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def findMid(head):
    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(list1, list2):
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


def sortList(head):
    # base case
    if head is None or head.next is None:
        return head
    # we have to break into two halves using mid nodes
    mid = findMid(head)
    left = head
    right = mid.next
    # break the List
    mid.next = None
    # sort RE
    # give left sorted list
    left = sortList(left)
    # give right sorted list
    right = sortList(right)
    # Merge both Left and Right LL
    mergeLL = merge(left, right)
    # mergeLL - head pointer
    return mergeLL
