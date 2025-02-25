'''
Largest BST in a Binary Tree
https://www.geeksforgeeks.org/largest-bst-binary-tree-set-2/
Given a Binary Tree, write a function that returns the size of the largest
subtree which is also a Binary Search Tree (BST).
If the complete Binary Tree is BST, then return the size of the whole tree.

-> Fast way to find diameter
-> balanced bst also fast way to find
using that pattern
all 3 - question solved
Pattern is Important

SOLN:
Binary Tree -> Sabse vada BST FIND
Multiple option - subtree

soln: Inorder -> sorted subset find max length
Recursive Soln:
Bottom Up APPROCH
Left ans
right ans
and node pe processing once get both ans

kya kya value ans me mila hoga
left tree is BST or not
right tree is BST or not
Node -> left me xota, right me vada
if all valid size change

KOI VI VYAKTI -> agar upar return kar raha haii to
4 - chij vata raha hoga
- is valid BST
- size
-> min value
-> max value kya haii

HAR NODE EK DATA RETURN -> node ke niche tak valid BST or not
   -> Valid BST
   -> maxVal
   -> minVal
   -> valid size
O(n)

'''


class NodeData:
    def __init__(self, size=0, minVal=float('-inf'), maxVal=float('inf'), validBST=False):
        self.size = size
        self.minVal = minVal
        self.maxVal = maxVal
        self.validBST = validBST


def largestBSTBT(root):
    # ans is passed byrefernce ans
    # bottom up
    global ans
    if root is None:
        # 4 chije return karna hoga
        temp = NodeData(0, float('-inf'), float('inf'), False)
        return temp
    leftAns = largestBSTBT(root.left)
    rightAns = largestBSTBT(root.right)
    # leftans, rightans aa gya
    # checking part and build current node ans
    # building current node ans
    currentNodeAns = NodeData()
    # +1 adding current node
    currentNodeAns.size = leftAns.size + rightAns.size + 1
    # max right me exit karta haii
    currentNodeAns.max = max(root.data, rightAns.max)
    # min value in left subtree
    currentNodeAns.min = max(root.data, leftAns.min)
    # checking valid BST
    # leftsubtree BST, rightsubtree BST, current BST
    if leftAns.validBST and rightAns.validBST and ((root.data > leftAns.maxVal) and (root.data < rightAns.minVal)):
        currentNodeAns.validBST = True
    else:
        currentNodeAns.validBST = False
    if currentNodeAns.validBST:
        ans = max(ans, currentNodeAns.size)
    return currentNodeAns
