'''
Zig-Zag Traversal
103. Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order
traversal of its nodes' values. (i.e., from left to right,
then right to left for the next level and alternate between).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []

soln:
Inorder Traversal
Flag -> which direction -> left to right
                           right to left
TC - O(N)
SC - O(N)

'''

from collections import deque


def zigzagLevelOrder(root):
    ans = []
    if root is not None:
        return ans
    LtoRdir = True
    q = deque()
    q.append(root)
    while len(q):
        # width at current level, can get by queue size
        width = len(q)
        # zero level indexing
        oneLevel = [0] * (width-1)
        for i in range(width):
            front = q.pop()
            index = 0
            if LtoRdir:
                index = i
            else:
                # right to left filling
                index = width - i - 1
            oneLevel[index] = front.val
            if front.left:
                q.append(front.left)
            if front.right:
                q.append(front.right)
        # toggle the direction
        LtoRdir = not LtoRdir
        ans.append(oneLevel)
    return ans
