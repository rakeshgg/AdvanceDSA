'''
Create BST using Inorder Traversal
BST INORDER - SORTED
Similar to Binary Search
mid node -> root node
left node
right node

1. case mid ko root bna dia
left right ko recursion karge

TC: N nodes create -> 1 node find than -> O(1)
total time: O(n)

'''


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bstUsingInorder(inorder, s, e):
    # base case
    # start end ko cross kar gya
    if s > e:
        return None
    mid = (s + e)//2
    element = inorder[mid]
    root = Node(element)
    # 1 case solved
    # left part recursion will do
    # similar to binary search
    root.left = bstUsingInorder(inorder, s, mid-1)
    root.right = bstUsingInorder(inorder, mid+1, e)
    return root


inorder = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = 0
e = 8
root = bstUsingInorder(inorder, s, e)
print(root.left.val)
