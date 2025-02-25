'''
Delete n nodes after skip m Nodes
https://www.geeksforgeeks.org/delete-n-nodes-after-m-nodes-of-a-linked-list/

Given a linked list and two integers M and N. Traverse the linked list
such that you retain M nodes then delete next N nodes, continue the same
till end of the linked list.
Difficulty Level: Rookie

Input:
M = 2, N = 2
Linked List: 1->2->3->4->5->6->7->8
Output:
Linked List: 1->2->5->6

Input:
M = 3, N = 2
Linked List: 1->2->3->4->5->6->7->8->9->10
Output:
Linked List: 1->2->3->6->7->8

Input:
M = 1, N = 1
Linked List: 1->2->3->4->5->6->7->8->9->10
Output:
Linked List: 1->3->5->7->9



'''


def skipMdeleteN(head, M, N):
    if head is None:
        return
    it = head
    for i in range(M-1):
        # if not availble M nodes
        if it is None:
            return
        it = it.next
    # it would be at mth node
    if it is None:
        return
    mthNode = it
    it = mthNode.next
    for i in range(N):
        if it is None:
            break
        temp = it.next
        it = temp
    mthNode.next = it
    # same work again and agin
    # Recursive call
    skipMdeleteN(it, M, N)
