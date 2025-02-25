'''
https://practice.geeksforgeeks.org/problems/transform-to-sum-tree/1
TransForm to Sum Tree

Given a Binary Tree of size N , where each node can have positive or
negative values. Convert this to a tree where each node contains the
sum of the left and right sub trees of the original tree. The values of
leaf nodes are changed to 0.

'''


def sumTree(root):
    if root is None:
        return 0
    # if leaf node
    if root.left is None and root.right is None:
        temp = root.data
        root.data = 0
        return temp
    lsum = sumTree(root.left)
    rsum = sumTree(root.right)
    temp = root.data
    root.data = lsum + rsum
    return root.data + temp


def toSumTree(node):
    sumTree(node)
