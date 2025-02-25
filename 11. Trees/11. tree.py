'''
ARE TWo TREE IDENTICAL

100. Same Tree

Given the roots of two binary trees p and q, write a function to
check if they are the same or not.

Two binary trees are considered the same if they are structurally
identical, and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3]
Output: true

Soln:
traverse both tree sath sath assuming identical

TWO NODES -> not equal to None !.e data hona chaiie dono
Data of node ka same hona chaiie

'''


def isSameTree(p, q):
    if p is None and q is None:
        return True
    if p is not None and q is not None:
        # check data
        return (p.val == q.val) and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    if p is None or q is None:
        return False


'''
Symmetric Tree or Mirror Tree
Mirror of itself

Given the root of a binary tree, check whether
it is a mirror of itself (i.e., symmetric around its center).

Mirror -> Left ko right, right ko left kar deta haii

'''


def isMirrorTree(p, q):
    if p is None and q is None:
        return True
    if p is not None and q is not None:
        # check data
        return (p.val == q.val) and isMirrorTree(p.left, q.right) and isMirrorTree(p.right, q.left)
    if p is None or q is None:
        return False


def isSymmetric(root):
    # assume root as pivot and divide into two parts
    # keep mirror in between root node
    return isMirrorTree(root.left, root.right)
