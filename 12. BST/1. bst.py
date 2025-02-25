'''
Create BST
Check it clearly

'''


class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def insertIntoBST(root, data):
    # every node can insert to max depth
    # AVG - O(logn)
    # worst - O(N)
    if root is None:
        # your Tree is Empty
        # this is first node we have to create
        root = Node(data)
        return root
    # first node nahi haii
    # decide to got left or right
    if root.data > data:
        # insert into Left
        root.left = insertIntoBST(root.left, data)
    else:
        # insert into right
        root.right = insertIntoBST(root.right, data)
    # return root
    return root


def takeInput(root):
    var = input("Enter something: ")
    data = int(var)
    # root = insertIntoBST(None, data)
    while data != -1:
        root = insertIntoBST(root, data)
        var = input("")
        data = int(var)
    return root


def preorder(root):
    # similary you can check
    # for inorder postorder
    if root is None:
        return
    print(root.data, end='-')
    preorder(root.left)
    preorder(root.right)


# searching
# if value grater than node go to right else left subtree
# AVG -> case O(H), H = LogN
# worst case -> O(N), H = N
def findNodeInBST(root, target):
    # rasta hi khatam ho gya
    # assuming there are unique value in Tree
    if root is None:
        return False
    if root.data == target:
        return True
    if target > root.data:
        # search in Right subtree
        return findNodeInBST(root.right, target)
    else:
        return findNodeInBST(root.left, target)


# Find Minimum value in any BST
# Approch 1 -> Inorder in sorted form store it -> min in front, max at end
# Approch 2 -> Recursion
# approch 3 -> root go to left left and where stop that is ans
#              root go to right right to get maximum
def minVal(root):
    temp = root
    if temp is None:
        return -1
    while temp.left is not None:
        temp = temp.left
    return temp.data


def maxVal(root):
    temp = root
    if temp is None:
        return -1
    while temp.right is not None:
        temp = temp.right
    return temp.data


def findNodeInBST1(root, target):
    if root is None:
        return None
    if root.data == target:
        return root
    if target > root.data:
        # search in Right subtree
        return findNodeInBST1(root.right, target)
    else:
        return findNodeInBST1(root.left, target)


# Deletion in BST
def deleteNodeInBST(root, target):
    # base case
    if root is None:
        return root
    if root.data == target:
        if root.left is None and root.right is None:
            # leaf node
            # temp ke jgh me None Lga dia
            return None
        elif root.left is None and root.right is not None:
            child = root.right
            # upar vej do child ko
            return child
        elif root.left is not None and root.right is None:
            child = root.left
            # upar vej do child ko
            return child
        else:
            # both child exit you can use either Inorder predessor or Inorder succesor
            # predessor Nikalna haii
            # inorder predessor left subtree max value
            inorderPre = maxVal(root.left)
            # replace with temp data
            root.data = inorderPre
            # need to delete inorderPre
            root.left = deleteNodeInBST(root.left, inorderPre)
            # jo vi deleteNodeInBST se bann ke ayega
            # tree usko root.left me laga lo
            return root
    elif target > root.data:
        # right jana haii
        # return right
        # right se delete kar ke jo vi nya tree bann raha haii usko
        # root ke right me lageo
        root.right = deleteNodeInBST(root.right, target)
    elif target < root.data:
        # left jaeo
        # nya tree jo delete ke bad banta haii wahh root.left
        # me laga te haii
        root.left = deleteNodeInBST(root.left, target)
    else:
        return root


if __name__ == '__main__':
    root = None
    print('Enter data for Node')
    root = takeInput(root)
    preorder(root)
    ans = findNodeInBST(root, 10)
    print(ans)
