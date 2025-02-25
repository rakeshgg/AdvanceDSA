'''
https://leetcode.com/problems/validate-binary-search-tree/
Validate BST
98. Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Input: root = [2,1,3]
Output: true

soln:
inorder -> sorted than binary search Tree
Inorder traversal -> O(n), O(h) Space
sorted check - O(n)

2nd approch: single pass
root -> range of values possible -> (-inf, inf) = 100
left node (-inf, 100) -> 50
left node (-inf, 50) -> 25
Har node ke lie range bata dia
if Every node range is valid than its valid BST


'''

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''


def solve(root, lb, ub):
    # base case
    if root is None:
        return True
    # jis node pe khada hu wahh range me haii ki nahi
    if root.val > lb and root.val < ub:
        # root data in range
        # 1 case solve sol rest part recursion will do
        leftAns = solve(root.left, lb, root.data)
        rightAns = solve(root.right, root.data, ub)
        # left and right dono BST hona chaiie
        return leftAns and rightAns
    else:
        return False


def isValidBST(root):
    lowerBound = float('-inf')
    upperBound = float('inf')
    ans = solve(root, lowerBound, upperBound)
    print(ans)
