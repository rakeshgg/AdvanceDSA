'''
110. Balanced Binary Tree

Given a binary tree, determine if it is
A height-balanced binary tree is a binary tree
in which the depth of the two subtrees
of every node never differs by more than one.

Input: root = [3,9,20,null,null,15,7]
Output: true

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def height(root):
    # base case
    if root is None:
        return 0
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    ans = 1 + max(leftHeight, rightHeight)
    return ans


def isBalanced(root):
    # need to check for every nodes diff is <= 1
    # node value not matters
    # har node left and right height and check diff
    # do for 1 node and for rest recursion will handle
    # base case
    if root is None:
        return True
    # solve 1 case
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    diff = abs(leftHeight - rightHeight)
    currNode = (diff <= 1)
    # recursion
    leftAns = isBalanced(root.left)
    rightAns = isBalanced(root.right)
    if currNode and leftAns and rightAns:
        return True
    else:
        return True
