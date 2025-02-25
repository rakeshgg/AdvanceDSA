'''
Merge K-Sorted Linked list
- Same logic as previous

23. Merge k Sorted Lists
You are given an array of k linked-lists lists, each
linked-list is sorted
in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

TC:nk*lon(nk)

'''

import heapq


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    # this is used by heap as comparactor operator
    def __lt__(self, other):
        return self.val < other.val


def mergeKLists(lists):
    minHeap = []
    # first k eleemnts insert
    k = len(lists)
    if k == 0:
        return None
    # first elemnts of every linked list insert in heap
    for i in range(k):
        # lists[i] is a pointer to linked list
        if lists[i] is not None:
            minHeap.append(lists[i])
    heapq.heapify(minHeap)
    head = None
    tail = None
    # 3 -step process
    # min heap empty
    while minHeap:
        temp = heapq.heappop(minHeap)
        # temp is it can be NULL not possible
        # we havent inserted NULL value
        # temp may or maynot be the first elemnts of answer linked list
        if head is None:
            # first elements of ans LL
            head = temp
            tail = temp
            if tail.next is not None:
                heapq.heappush(minHeap, tail.next)
        else:
            # temp is not first elements of LL
            tail.next = temp
            tail = temp
            if tail.next is not None:
                heapq.heappush(minHeap, tail.next)
    return head
