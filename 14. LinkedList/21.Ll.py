'''
https://leetcode.com/problems/merge-nodes-in-between-zeros/
2181. Merge Nodes in Between Zeros

You are given the head of a linked list, which contains a series of
integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them
into a single node whose value is the sum of all the merged nodes.
The modified list should not contain any 0's.

Return the head of the modified linked list.

Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation:
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.

SOLN: 2 Pointer Approch

'''


def mergeNodes(head):
    if head is None:
        return head
    slow = head
    fast = head.next
    newLastNode = None
    sum = 0
    while fast:
        if fast.val != 0:
            sum += fast.val
        else:
            # if fast is zero
            # two consecutive zero found
            # sum should be set to slow position
            slow.val = sum
            lastNode = slow
            slow = slow.next
            sum = 0
        fast = fast.next
    temp = lastNode.next
    # just formed new List
    newLastNode.next = None
    # deleting old list
    while temp is not None:
        nxt = temp.next
        temp = nxt
