'''
sorted linked list how to convert in bst
soln
sorted array - wala approch
Recursion:
1 node attach karo tree me baki Recursion karega

Big problem -> (head, n)
        (head, n-1-n/2), (head, n/2)
pahle right part solve karne pe left wala part bar bar traversal
karna padega so left wala pahle solve karna haii

TC -> O(N)
SC -> O(H), Recursion stack

'''


def sortedLLIntoBST(head, n):
    # head is by refernce -> head in c++
    # base case LL EMPTY
    if n <= 0 or (head is None):
        return None
    leftSubtree = sortedLLIntoBST(head, n - 1 - n//2)
    # root node
    root = head
    root.left = leftSubtree
    # head ek step aage point right
    # head ko age vadhana vull jate haii
    head = head.right
    # head right wali LL ke starting point pe pauch gya
    # solving right part
    root.right = sortedLLIntoBST(head, n//2)
    return root
