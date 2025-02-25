'''
https://leetcode.com/problems/path-sum-ii/

113. Path Sum II

Given the root of a binary tree and an integer targetSum, return all
root-to-leaf
paths where the sum of the node values in the path equals targetSum. Each path
should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any
leaf node. A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Input: root = [1,2,3], targetSum = 5
Output: []

SOLN: use List during call, sum


'''


def solve(root, targetSum, currSum, path, ans):
    # base case
    if root is None:
        return
    # if leaf node
    if root.left is None and root.right is None:
        # current sum dekhna tha
        if currSum == targetSum:
            # add leaf node also
            path.append(root.val)
            currSum += root.val
            ans.append(path)
            return
    # include current node
    path.append(root.val)
    currSum += root.val
    # recursive call
    solve(root.left, targetSum, currSum, path, ans)
    solve(root.right, targetSum, currSum, path, ans)


# if currSum and path is passd as by refernce that is global
# path is mutable so its global so backtracking is required
# than backtracking is required
def solve2(root, targetSum, path, ans):
    # base case
    global currSum
    if root is None:
        return
    # if leaf node
    if root.left is None and root.right is None:
        # current sum dekhna tha
        if currSum == targetSum:
            path.append(root.val)
            currSum += root.val
            # required copy of path
            ans.append(path[:])
            # backtrack
            path.pop()
            currSum -= root.val
            return
    path.append(root.val)
    currSum += root.val
    solve2(root.left, targetSum, path, ans)
    solve2(root.right, targetSum, path, ans)
    # backtrack
    path.pop()
    currSum -= root.val


def pathSum(root, targetSum):
    ans = []
    sum = 0
    path = []
    solve(root, targetSum, sum, path, ans)
    return ans
