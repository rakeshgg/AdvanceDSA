'''
Vertical Order Traversal
987. Vertical Order Traversal of a Binary Tree

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at
positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the
tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom
orderings for each column index starting from the leftmost column and ending
on the rightmost column. There may be multiple nodes in the same row and same
column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.

soln:
Imagine Tree as a grid
level - row
vertical - col
col
-2
-1
0
1
2
map is keywise sorted
map -> col -> map(row, multiset)
col is sorted wise
row wise sorted

'''


from collections import deque
from collections import OrderedDict
from collections import defaultdict


def verticalTraversal(root):
    ans = []
    # store pairs node, row, col
    q = deque()
    q.append((root, 0, 0))
    # map col rowwise sorted
    # col -> row:[x, y, z]
    mp = OrderedDict()
    while len(q):
        front = q.pop()
        node, coordinate = front
        row, col = coordinate
        if col not in mp:
            mp[col] = defaultdict(lambda: [])
        mp[col][row].append(node.val)
        # level order push bari bari
        if node.left:
            # row + 1, col - 1
            q.append((node.left, row+1, col+1))
        if node.right:
            q.append((node.right, row+1, col+1))
    # store final vertical order into ans
    for col, row in mp.items():
        vertOrder = mp.get(row)
        if vertOrder:
            ans.append(vertOrder)
