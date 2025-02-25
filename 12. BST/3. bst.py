'''
LCA OF BST
Lowest Common Ancestor

is same logic applied as previous binary tree - yes, but extra work
p, q -> find p and q
        during return both meet at a point !.e LCA

BST -> Inorder Sorted
    -> left smaller, right greater
using this Find better solutions
4-CASE

1. p,q is less than root data, dono lie in left, call should be Left
2. p,q is grater than root data, dono lie in right, call should be Right
3. p less than root data, q greater than root data, P left, q right than root is ans
4. p is greater than root data, q is lesser than root data, root is ans

Simple CASE:
don't confuse in BST and Binary Tree

235. Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is
defined between two nodes p and q as the lowest node in T that has both p and q
as descendants (where we allow a node to be a descendant of itself).”

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

'''


def lowestCommonAncestor(root, p, q):
    # base case
    if root is None:
        return None
    # case 1
    if p.data < root.data and q.data < root.data:
        # ans lie in left
        return lowestCommonAncestor(root.left, p, q)
    # case 2
    if p.data > root.data and q.data > root.data:
        return lowestCommonAncestor(root.right, p, q)
    # rest part me root ans
    # case 3 and 4
    return root
