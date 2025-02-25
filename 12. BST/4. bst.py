'''
kth smallest elements in BST
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k,
return the kth smallest value (1-indexed) of all the values
of the nodes in the tree.

Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

SOLn
APPROCH1: Store inorder and find kth, TC:O(N), SC:O(N)
APPROCH2: LNR can be done recursive - On recturn k --, if k == 0 ans

'''


def kthSmallest(root, k):
    # k should pe passed as by refernce
    # if not byrefernce than backtrack
    # base case
    if root is None:
        # -1 reflects base condition reach
        return -1
    # Inorder
    # left call
    leftAns = kthSmallest(root.left, k)
    if leftAns != -1:
        return leftAns
    # root call
    k = k-1
    if k == 0:
        return root.data
    # right ka call
    rightAns = kthSmallest(root.right, k)
    return rightAns


def kthSmallest1(root):
    global k
    # k should pe passed as by refernce
    # base case
    if root is None:
        # -1 reflects base condition reach
        return -1
    # Inorder
    # left call
    leftAns = kthSmallest1(root.left)
    # valid ans leftAns
    if leftAns != -1:
        return leftAns
    # root call
    k = k-1
    if k == 0:
        return root.data
    # right ka call
    rightAns = kthSmallest1(root.right)
    # valid ans assume
    return rightAns
