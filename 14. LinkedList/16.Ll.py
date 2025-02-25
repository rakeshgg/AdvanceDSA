'''
Flatten Linked List -> Similar to Merge Two linked LIST
https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1

Given a Linked List of size N, where every node represents a sub-linked-list
and contains two pointers:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.
Each of the sub-linked-list is in sorted order.
Flatten the Link List such that all the nodes appear in a single level
while maintaining the sorted order.

Note: The flattened list will be printed using the bottom pointer instead of the next pointer.
For more clarity have a look at the printList() function in the driver code.

Input:
5 -> 10 -> 19 -> 28
|     |     |     |
7     20    22   35
|           |     |
8          50    40
|                 |
30               45
Output:  5-> 7-> 8- > 10 -> 19-> 20->
22-> 28-> 30-> 35-> 40-> 45-> 50.
Explanation:
The resultant linked lists has every
node in a single level.
(Note: | represents the bottom pointer.)

Merge - N sorted List
consider 1, 2 sublist = ans
consider ans, 3 sublist

ALGO:
- Main Linked list 1st two node pick, root - L1, root.next - L2
- Merge with L1, L2


'''


def mergeList(a, b):
    if not a:
        return b
    if not b:
        return a
    # 1 case samhalenge baki recursion karega
    ans = None
    if a.data < b.data:
        ans = a
        a.bottom = mergeList(a.bottom, b)
    else:
        ans = b
        b.bottom = mergeList(a, b.bottom)
    return ans


def flattern(root):
    # merge from backward
    if root is None:
        return root
    # pixe ja kar merge kar rahe haii
    # pixe se karne se pointer nahi bachna hota haii jo node next point karta haii
    # next list me
    mergeLL = mergeList(root, flattern(root.next))
    return mergeLL
