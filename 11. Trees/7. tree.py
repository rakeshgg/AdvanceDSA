'''
using
Preorder -> N L R
inorder -> L N R
Buid the Tree

-> create root node
-> Preorder -> Find Root, sabse pahla node root hi hoga
-> Inorder -> Find Left, Right Subtree

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findPosition(arr, n, elements):
    for i in range(n):
        if arr[i] == elements:
            return i
    return -1


# Build Tree from Inorder/Preorder Travsersal
# issue preIndex should pass by refernce than this code work
# but why ek bar aap preIndex me aage vadd chuke haii to waps
# nahi ana haii pixe aate kab jab call by value hota so
# jaha par preIndex aage ja chuka haii wahi apne state ko maintin kare
def buildTreeInPre(inorder, preorder, size, preIndex, inoStart, inoEnd):
    # base case
    if preIndex >= size or inoStart > inoEnd:
        return None
    # step A
    print(preIndex)
    element = preorder[preIndex]
    preIndex += 1
    # make root to elemnts
    root = TreeNode(element)
    # want to solve left and right part
    pos = findPosition(inorder, size, element)

    # Step B solve Root Left Recursion dekhega
    root.left = buildTreeInPre(inorder, preorder, size, preIndex, inoStart, pos-1)
    # Step c solve Root Right Recursion dekhega
    root.right = buildTreeInPre(inorder, preorder, size, preIndex, pos+1, inoEnd)
    return root


def buildTreeInPreGlobal(inorder, preorder, size, inoStart, inoEnd):
    # base case
    global preIndex
    if preIndex >= size or inoStart > inoEnd:
        return None
    # step A
    print(preIndex)
    element = preorder[preIndex]
    preIndex += 1
    # make root to elemnts
    root = TreeNode(element)
    # want to solve left and right part
    pos = findPosition(inorder, size, element)

    # Step B solve Root Left Recursion dekhega
    root.left = buildTreeInPreGlobal(inorder, preorder, size, inoStart, pos-1)
    # Step c solve Root Right Recursion dekhega
    root.right = buildTreeInPreGlobal(inorder, preorder, size, pos+1, inoEnd)
    return root

# optimization scope any
# position finding O(n) -> O(1) using dictionary
# create map before building tree


def buildTreeInPostGlobal(inorder, postorder, size, inoStart, inoEnd):
    global posIndex
    # base case
    if posIndex < 0 or inoStart > inoEnd:
        return None
    element = preorder[posIndex]
    posIndex -= 1
    # make root to elemnts
    root = TreeNode(element)
    pos = findPosition(inorder, size, element)
    root.right = buildTreeInPostGlobal(inorder, postorder, size, pos+1, inoEnd)
    root.left = buildTreeInPostGlobal(inorder, postorder, size, inoStart, pos-1)
    return root


def Traversal(root):
    if root is None:
        return
    print(root.val)
    Traversal(root.left)
    Traversal(root.right)


inorder = [40, 20, 50, 10, 60, 30, 70]
preorder = [10, 20, 40, 50, 30, 60, 70]
size = 7
preIndex = 0
inoStart = 0
inoEnd = size-1
# root = buildTreeInPre(inorder, preorder, size, preIndex, inoStart, inoEnd)
# root = buildTreeInPreGlobal(inorder, preorder, size, inoStart, inoEnd)
# Traversal(root)
inorder = [40, 20, 10, 50, 30, 60]
postorder = [40, 20, 50, 60, 30, 10]
size = 6
posIndex = size - 1
inoStart = 0
inoEnd = size-1
root = buildTreeInPostGlobal(inorder, postorder, size, inoStart, inoEnd)
Traversal(root)
