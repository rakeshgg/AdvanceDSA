'''
110. Balanced Binary Tree
Height balanced Tree
Given a binary tree, determine if it is
height-balanced

Height =  abs(lh - rh) <= 1

Every Node left height, right height
height also call n times
so optimize
-> Height function: always bottom up

'''


def height(root):
    global is_balanced
    if root is None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    # check height balaned condition
    # for currentNode
    if is_balanced and abs(lh-rh) > 1:
        # for one node if its false than
        # never check again
        is_balanced = False
    currentheight = 1 + max(lh, rh)
    return currentheight


def isBalanced(root):
    # optimized form O(N)
    # height function used
    is_balanced = True
    height(root)
    return is_balanced
