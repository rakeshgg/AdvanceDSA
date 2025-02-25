'''
DFS/BFS in Implicit Graph
- Grid made of 0's and 1's - each cell go to 4 direction
- grid can be represented by graph

'''

# Templtes
'''
graph = {}
for i in [0, n)
   for j in [0, m)
       graph[(i, j)] - []
       for each adjacent cell(nexti, nextj)
           if grid[nexti][nextj] exists and not a wall
              graph[(i, j)].add((nexti, nextj))
dfs(graph, (0, 0))

just need 2 things to apply BFS/DFS
how vertices represented
how to find neighbours of vertices

i = row
j = col

4 - direction edges     -|--

0 - open
1 - block

'''

'''
def dfs(grid, i, j, visited):
    # i, j is corodinate from where we start
    n, m = len(grid), len(grid[0])
    # tuple as coordinate
    visited.add((i, j))
    print(i, j)
    # need to traaverse the neighbours that is adjacen cell of cell
    # we can take 4 - direction in nay order bootom, top, right, left say
    adjacent_cells = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    for (next_i, next_j) in adjacent_cells:
        # cell shoud be inside the grid
        # bodundary condition need to be handle
        if 0 <= next_i < n\
            and 0 <= next_j < m\
            and grid[next_i][next_j] == 0\
            and (next_i, next_j) not in visited:
                dfs(grid, next_i, next_j, visited)
                # then next_i, next_j is neighbour of i and j
                # need to move from i, j to next_i, next_j


def grid_dfs(grid, i, j):
    visited = set()
    dfs(grid, i, j, visited)
'''


BFS

def grid_dfs(grid, i, j):
   n, m = len(grid), len(grid[0])
   visted = set()
   queue = Queue()
   queue.put((i,j))
   visited.add((i, j))
   while not queue.empty():
       i, j = queue.get()
       print(i, j)
       adjacent_cells = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
       for (next_i, next_j) in adjacent_cells:
        # cell shoud be inside the grid
        # bodundary condition need to be handle
        if 0 <= next_i < n\
            and 0 <= next_j < m\
            and grid[next_i][next_j] == 0\
            and (next_i, next_j) not in visited:
                queue.put((next_i, next_j))
                visited.add((next_i, next_j))



- Flood Fill Algprithums - DFS/BFS
- Maize Problems - DFS/BFS

- How Vertex represented
- How to Access neighbour
