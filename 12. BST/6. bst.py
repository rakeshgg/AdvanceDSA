'''
I have a BST tree

653. Two Sum IV - Input is a BST
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST
such that their sum is equal to k, or false otherwise.

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

soln:
lets suppose one number is 200
traget = 320

root-> target - root, search and find
1st node traversal -> n options for every option search - search complexity avg: O(logn)
balanced case -> O(nlogn)

Approch2: Inorder sorted
sorted array, s = 0, end = len(arr) - 1
sum of both and find TWO pointer Approch
-> O(N)

'''


def storeInorder(root, inorder):
    if root is None:
        return
    storeInorder(root.left, inorder)
    inorder.append(root.data)
    storeInorder(root.right, inorder)


def findTarget(root,  k):
    inorder = []
    storeInorder(root, inorder)
    # using two pointer approch
    s = 0
    e = len(inorder) - 1
    while s < e:
        # <= s, e point same so can't take sum of both
        sum = inorder[s] + inorder[e]
        if sum == k:
            return True
        if sum > k:
            e = e - 1
        else:
            s = s + 1
    return False
