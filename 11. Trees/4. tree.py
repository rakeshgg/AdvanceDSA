'''
https://practice.geeksforgeeks.org/problems/kth-ancestor-in-a-tree/1
https://www.geeksforgeeks.org/kth-ancestor-node-binary-tree/

SOLN:
Find P
and Go to K - Steps Up you found the ans

Finding P -> Any Traversal you can use

jab wapas jaeo k-- kar do
if k == 0 milega that is ans

'''


def getKthAncestor(root, k, p):
    # base case
    if root is None:
        return False
    if root.data == p.data:
        return True
    leftAns = getKthAncestor(root.left, k, p)
    rightAns = getKthAncestor(root.right, k, p)
    # kyse pata chlega k mila ki nahi
    # store kar lo so leftAns, rightAns
    # jab returnho raha haii tab k ko minus kar rahe haii
    if leftAns or rightAns:
        k = k - 1
    if k == 0:
        print(root.data)
        # once you get zero set k to -1
        # so that k will change and never be zero
        k = -1
    return leftAns or rightAns


def getKthAncestor2nd(root, k, p):
    # use list on call store data in a list
    # once node found on return pop data from list
    # k times you will get ans
    pass
