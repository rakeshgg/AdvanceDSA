'''
K-Path SUM

437. Path Sum III

Given the root of a binary tree and an integer targetSum, return the number
of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must
go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Soln:
BreakDown Question:
is there exit path from root

TC -> O(n^2)


'''


def pathFromOneRoot(root, targetSum):
    global ans
    if root is None:
        return
    # preorder traversal
    if targetSum == root.val:
        ans += 1
    pathFromOneRoot(root.left, targetSum - root.val)
    pathFromOneRoot(root.right, targetSum - root.val)


def pathSum(root, targetSum):
    '''
    ans = 0
    pathFromOneRoot(root, targetSum)
    print(ans)
    '''
    # check for very node path
    # preorder Traversal
    # evry node can be root
    ans = 0
    if root is not None:
        pathFromOneRoot(root, targetSum)
        pathSum(root.left, targetSum)
        pathSum(root.right, targetSum)
    print(ans)
