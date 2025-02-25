'''
Copy List with random Pointer/Clone Linked List
https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly
n brand new nodes, where each new node has its value set to the value of
its corresponding original node. Both the next and random pointer of the
new nodes should point to new nodes in the copied list such that the pointers
in the original list and copied list represent the same list state. None of the
pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list,
where X.random --> Y, then for the corresponding two nodes x and y
in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes.
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the
random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

SOLN:
Recursively assign next and create LL
how random is assigned
- during copying LL next, create a MAP
  oldPtr, newPtr
  purani node se naya list ka node ka mapping haii
- using this assign random pointers

TC - Recursively Iterative ones -> O(N)
SC - N enries in MAP, recursion call = O(N)

Can we make space complexity from O(N) - O(1)

'''


class Node:
    def __init__(self, x, next, random):
        self.val = int(x)
        self.next = next
        self.random = random


def helper(head, mp):
    # sc - O(N)
    if head is None:
        return head
    newHead = Node(head.val)
    mp[head] = newHead
    # recursion dekho vai
    newHead.next = helper(head.next, mp)
    # random pointer assigned
    if head.random is not None:
        newHead.random = mp[head.random]
    return newHead


def helperNew(head, mp):
    # SC - O(1) - without map
    # chnage the linked list if map not use
    # 7 - 7 - 13- 13- 11 - 11
    # oldnode - newnode
    '''
    1. clone list make point oldnode - newnode
    2. newnode random pointer need to point using old random pointer
    3. Assign random pointer to new node with help of old node
    4.deattach old list with new list
    '''
    if head is None:
        return head
    # clone A to A'
    # iterate over old head
    it = head
    while it is not None:
        clonedNode = Node(it.val)
        clonedNode.next = it.next
        it.next = clonedNode
        it = it.next.next
    # Assign random link of A's with help of old node A
    it = head
    while it is not None:
        clonedNode = it.next
        if it.random is not None:
            clonedNode.random = it.random.next
        # move it
        it = it.next.next
    # detach A' from A
    it = head
    clonedhead = it.next
    while it is not None:
        clonedNode = it.next
        it.next = it.next.next
        if clonedNode.next is not None:
            clonedNode.next = clonedNode.next.next
    return clonedhead


def copyRandomList(head):
    # store oldNode, newNode mapping
    map = {}
    return helper(head, map)
