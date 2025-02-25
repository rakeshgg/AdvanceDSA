'''
257. Binary Tree Paths

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Input: root = [1]
Output: ["1"]


'''


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root, ans, temp):
    # base case
    if root is None:
        return
    # if root is leaf
    if root.left is None and root.right is None:
        # store ans
        temp += str(root.val)
        ans.append(temp)
        return ans
    # standing on any node
    oldTemp = temp
    temp = temp + str(root.val)
    temp += '->'
    solve(root.left, ans, temp)
    solve(root.right, ans, temp)
    # all above changes need to be removed on backtrack
    # so above one variable need to created
    # which track the old data
    temp = oldTemp


def binaryTreePaths(root):
    '''
    return is of string form
    at staring its empty string
    backtrack - addition jo kia tha usko pop
    karna padega

    '''
    ans = []
    temp = ''
    solve(root, ans, temp)
