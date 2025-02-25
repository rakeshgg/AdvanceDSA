'''
GFG
Check whether Binary Tree is Sum Tree or not
Convert binary tree into Sum Tree

SUM TREE -> current Node -> replace with leftsubtree sum + right subtree sum
                        + current Node
if NUll -> 0

Left Subtree SUM + Current value + Right Subtree SUM

'''


def ConvertIntoSubTree(root):
    if root is None:
        return 0
    leftAns = ConvertIntoSubTree(root.left)
    rightAns = ConvertIntoSubTree(root.right)
    root.data = leftAns + root.data + rightAns
    # return root.data !.e sum to next node
    return root.data
