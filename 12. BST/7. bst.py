'''
Convert BST in Sorted Doubly Linked List
inorder - Sorted using that create new node
but what if inplace is Required

Using Recursion:SOLN
RootNode -> RightSubtree solve -> Linked LIST

RootNode -> LNR

right subtrre solve
root attach
left subtree

'''


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# head = None - LL
# root - TREE
def convertIntoSortedDLL(root, head):
    # head should be passed by reference
    # Global head
    # base case
    if root is None:
        return
    # convert Right subtree in LL
    convertIntoSortedDLL(root.right, head)
    # attch root node
    root.right = head
    # head ke prev vi to root pr lagan haii
    if head is not None:
        head.left = root
    # update LL head
    head = root
    # left Subtree Linked list
    convertIntoSortedDLL(root.left, head)


def printLL(head):
    temp = head
    while temp is not None:
        print(temp.val)
        temp = temp.right
