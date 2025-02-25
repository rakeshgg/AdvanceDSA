'''
Diagonal Traversal of Binary Tree

Consider lines with a slope of -1 that cross through nodes.
Print all diagonal elements in a binary
tree that belong to the same line, given a binary tree.

Output :
Diagonal Traversal of binary tree:
 8 10 14
 3 6 7 13
 1 4
Observation : root and root->right values
will be prioritized over all root->left values.

Better ways:
Numbering the Tree -> Going Left +1
                      Going Right do nothing
yes print all 0's mark -> 1 diagonal
yes print all 1's mark -> 2nd diagonal
yes print all 2's mark -> 3rd diagonal

d = 0, pass as arguments
store in map -> by default key sorted

if d == 0:
   push on map
once traversal done -> than print it
def diagonal(root, map, d):
    pass

2nd Ways:
using level order traversal
-> pushed root
-> if left exit pushed
-> if right exit pushed
now pahle right push ho rahe haii
than left
pop -> temp
while temp
   print(temp)
   if temp.left
     # will see latter
     q.append()
   # traverse
   temp = temp.right
Quee se elemnts nikalte haii right print karte haii
koi left milta haii to push karte haii queue me

'''

from collections import deque


def diagonal(root, map, d):
    ans = []
    if root is not None:
        return ans
    q = deque()
    q.append(root)
    while len(q):
        temp = q.pop()
        while temp is not None:
            ans.append(temp.data)
            if temp.left:
                q.append(temp.left)
            temp = temp.right
    return ans
