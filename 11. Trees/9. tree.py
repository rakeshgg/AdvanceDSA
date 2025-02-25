'''
Diameter of Trees -> any node left depth + right depth do for all node
                     and maximum among them is a daimeter
                     Longest path from Node to Node

543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number
of edges between them.

'''


def maxDepth(root):
    # max depth function called on every nodes
    if root is None:
        return 0
    leftHeight = maxDepth(root.left)
    rightHeight = maxDepth(root.right)
    ans = max(leftHeight, rightHeight) + 1
    return ans


def diameterOfBinaryTree(root):
    # TC -> O(n^2)
    if root is None:
        return 0
    op1 = diameterOfBinaryTree(root.left)
    op2 = diameterOfBinaryTree(root.right)
    op3 = maxDepth(root.left) + 1 + maxDepth(root.right)
    ans = max(op1, op2, op3)
    return ans


def height(root):
    global diameter
    if root is None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    # diametr
    currD = lh + rh
    # max diameter
    diameter = max(diameter, currD)
    return max(lh, rh) + 1


def diameterOfBinaryTreeOptim(root):
    # HT function
    # left HT, Right HT required
    # keep track of height on tha way for finding diameter
    # TC -> O(N)
    diameter = 0
    height(root)
    return diameter
