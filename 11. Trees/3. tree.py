'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given
nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor
is defined between two nodes p and q as the lowest node in T that has both
p and q as descendants (where we allow a node to be a descendant of itself).”


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a
descendant of itself according to the LCA definition.

Input: root = [1,2], p = 1, q = 2
Output: 1

LCA: for two node p, q
-> Ancestor -> poorvaj tree me upar milte haii node se
-> Ancestor me node se upar jana hota haii root tak
          jo node milte haii wahh ancestor hota haii
-> P ancestor
-> q ancestor
-> get common
-> lowest me sabse pahle jo mita haii path me

HIT AND TRIAL METHODS
# Tree me Recursion chaleo aur dry run ke dekho
-> p tak pauchna padega
-> jab waha se wapas aunga tavi to ancestor milega
-> Random Try what to return

4- cases:
lCA, p left, q right
lCA  q left, p right
lCA  p, q left
lCA  p, q right

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root, p, q):
    # base case
    if root is None:
        return None
    # any node we stand left, right First check that node is p or q
    # check p, q
    if root.val == p.val:
        return p
    if root.val == q.val:
        return q
    # if not find above than leftans, rightAns
    leftAns = lowestCommonAncestor(root.left, p, q)
    rightAns = lowestCommonAncestor(root.right, p, q)
    if leftAns is None and rightAns is None:
        # p and q not in a tree
        return None
    elif leftAns is not None and rightAns is None:
        return leftAns
    elif leftAns is None and rightAns is not None:
        return rightAns
    elif leftAns is not None and rightAns is not None:
        # you found LCA
        # return current Node
        return root
