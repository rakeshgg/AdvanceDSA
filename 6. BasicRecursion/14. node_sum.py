'''
sum of node in Linked list

'''


def nodeSum(root):
    if root is None:
        return 0
    return root.data + nodeSum(root.next)
