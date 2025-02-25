'''
LEC - 175
Views in Tree
-> c- how to use map
->

Top View: - Upar se niche ke tarf se dekhna
 Input:     1
           /  \
         2     3
       /  |   / \
     4    5  6   7

Output: Top view of the above binary tree is: 4 2 1 3 7
NOTE: Upar se niche direction me
Horizoantal distance Concept -> root se distance
Level
these concepts are used in Views
root - hd =0
let make rule -> if goes left hd - 1
                 if goes right hd + 1
        NLR Traversal -> Fit nahi baith raha haii
        level Order -> Higher order already traversal
                       This will work

        Vertical line in same node

Bottom View -> Tree ko niche se dekh raha hu
-> HD, Left, right

printLeftView -> Recursively doing
              -> HD not Required
    kisi vi Level pe khada hu
    than har level ka 1st node is Left view
    left view -> process left first
    # kisi node pe khade haii Level 0 ans
    # level 1, left store level1 ans
    # if ans exit for level dont update it
    -> you can do using maps also
printRightView

Boundary Traversal:
-> Print Left part first - level order >
-> print all leaf nodes second
-> print all right nodes in reverse order
Logic:
print left part first -> stop on leaf -> preorder kind up
if no left -> go to right part


'''


from collections import deque
from collections import OrderedDict


def printTopView(root):
    if root is None:
        return
    # map to store horizaontal distance according top node
    # create a map for storing HD -> Top Node data
    topNode = OrderedDict()
    # Level order
    # we will store a tuple consisting of node and HD
    q = deque()
    # push initial value in queue
    q.append((root, 0))
    while len(q):
        temp = q.pop()
        frontNode, hd = temp
        # is frontNode is ans or not
        # jo bhi HD aya haii check if ans for that HD already exists or not
        # extra condition in Level order to make Top View
        if not topNode.get(hd):
            # create entry
            topNode[hd] = frontNode.data
        # Level order traversal
        if frontNode.left:
            q.append((frontNode.left, hd-1))
        if frontNode.right:
            q.append((frontNode.right, hd+1))
    # ans stored in MAP
    print(topNode)


def printBottomView(root):
    if root is None:
        return
    # map to store horizaontal distance according top node
    # create a map for storing HD -> Top Node data
    topNode = OrderedDict()
    # Level order
    # we will store a tuple consisting of node and HD
    q = deque()
    # push initial value in queue
    q.append((root, 0))
    while len(q):
        temp = q.pop()
        frontNode, hd = temp
        # is frontNode is ans or not
        # jo bhi HD aya haii check if ans for that HD already exists or not
        # extra condition in Level order to make Top View not required in BV
        # if not topNode.get(hd)
        topNode[hd] = frontNode.data
        # Level order traversal
        if frontNode.left:
            q.append((frontNode.left, hd-1))
        if frontNode.right:
            q.append((frontNode.right, hd+1))
    # ans stored in MAP
    print(topNode)


def printLeftView(root, ans, level):
    if root is None:
        return
    if level == len(ans):
        ans.append(root.data)
    # left Tree
    printLeftView(root.left, ans, level+1)
    printLeftView(root.right, ans, level+1)


def printRightView(root, ans, level):
    if root is None:
        return
    if level == len(ans):
        ans.append(root.data)
    # right call pahle karna haii
    printRightView(root.right, ans, level+1)
    printRightView(root.left, ans, level+1)


def printLeftBoundary(root):
    # base case
    # if root is None go back
    if root is None:
        return
    # stop leaf node than go back
    if root.left is None and root.right is None:
        return
    print(root.data)
    if root.left:
        printLeftBoundary(root.left)
    else:
        # if left not exist than right
        printLeftBoundary(root.right)


def printLeafBoundary(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.data)
    printLeafBoundary(root.left)
    printLeafBoundary(root.right)


def printRightBoundary(root):
    # base case
    if root is None:
        return
    if root.left is None and root.right is None:
        return
    # pahle right agar nahi exit than left
    if root.right:
        printRightBoundary(root.right)
    else:
        printRightBoundary(root.left)
    print(root.data)


def boundaryTraversal(root):
    if root is None:
        return
    # duplicacy bachyega e print
    print(root.data)
    # A
    printLeftBoundary(root.left)
    # b
    printLeafBoundary(root)
    # c
    printRightBoundary(root.right)
