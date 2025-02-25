"""
Shortest Path -> Disktra Algo
let say undirtcted weighted graph

shortest path from source to destination
SOLN:
if weight not given -> by default 1 to all
BFS -> level order
Observation: BFS dwara kisi vi node pe pauchate haii
sabse pahle visit hua hota haii wahi shortest path haii
source to destination: sabse pahle destination me pauchte
ho wahi shortest path haii
how to find path:
parent, visited
-> source insert



"""

from collections import defaultdict
from collections import deque


class Graph:
    # 0 ke corresponding neighbors store karna haii
    def __init__(self):
        self.adjList = defaultdict(lambda: [])

    def addEdgeWeight(self, u, v, weight, direction):
        self.adjList[u].append((v, weight))
        if direction == 0:
            self.adjList[v].append((u, weight))

    def printAdjaencyList(self):
        for key, value in self.adjList.items():
            print(key, " ->", value)

    def shortestPathBfs(self, src, dest):
        # O(E+V)
        q = deque()
        visited = defaultdict(lambda: 0)
        parent = {}
        # inital step for src
        q.append(src)
        visited[src] = 1
        # used for path finding
        parent[src] = -1
        while len(q):
            frontNode = q.popleft()
            for nbr in self.adjList[frontNode]:
                if not visited[nbr[0]]:
                    q.append(nbr[0])
                    visited[nbr[0]] = 1
                    parent[nbr[0]] = frontNode
        # path print from dest
        ans = []
        node = dest
        print(parent)
        while node != -1:
            ans.append(node)
            node = parent[node]
        ans.reverse()
        print(ans)
        # [0, 6, 7, 8, 4]

    def topoSortDFS(self, src, visited, stack):
        print(src, end=" -> ")
        visited[src] = True
        for neighbor in self.adjList[src]:
            if not visited.get(neighbor[0]):
                self.topoSortDFS(neighbor[0], visited, stack)
        # while returning store in stack
        # store current node
        stack.append(src)

    def shortestPathDfs(self, dest, topoOrder, n):
        # 0 se 2 option 1 or 2
        dist = [float("inf")] * n
        src = topoOrder.pop()
        dist[src] = 0
        # ans need to set for source
        # if anything pop from stack than neighbor distance updated
        for nbr in self.adjList[src]:
            if dist[src] + nbr[1] < dist[nbr[0]]:
                dist[nbr[0]] = dist[src] + nbr[1]
        while len(topoOrder):
            topElement = topoOrder.pop()
            # distance array to update
            # update if valid distance is there
            if dist[topElement] != float("inf"):
                for nbr in self.adjList[topElement]:
                    # update distnace of neighbor
                    if dist[topElement] + nbr[1] < dist[nbr[0]]:
                        dist[nbr[0]] = dist[topElement] + nbr[1]

        for i in range(n):
            print(i, " -> ", dist[i])


G = Graph()
G.addEdgeWeight(0, 1, 1, 1)
G.addEdgeWeight(1, 2, 1, 1)
G.addEdgeWeight(2, 3, 1, 1)
G.addEdgeWeight(3, 4, 1, 1)
G.addEdgeWeight(0, 5, 1, 1)
G.addEdgeWeight(5, 4, 1, 1)
G.addEdgeWeight(0, 6, 1, 1)
G.addEdgeWeight(6, 7, 1, 1)
G.addEdgeWeight(7, 8, 1, 1)
G.addEdgeWeight(8, 4, 1, 1)
G.printAdjaencyList()
print("\n")

src = 0
dest = 4
G.shortestPathBfs(src, dest)

# directed graph
G = Graph()
G.addEdgeWeight(0, 1, 5, 1)
G.addEdgeWeight(0, 2, 3, 1)
G.addEdgeWeight(2, 1, 2, 1)
G.addEdgeWeight(1, 3, 3, 1)
G.addEdgeWeight(2, 3, 5, 1)
G.addEdgeWeight(2, 4, 6, 1)
G.addEdgeWeight(4, 3, 1, 1)
G.printAdjaencyList()

visited = defaultdict(lambda: False)
topoOrder = []
G.topoSortDFS(0, visited, topoOrder)
print("\n")
print("topo", topoOrder)
dest = 3
G.shortestPathDfs(dest, topoOrder, 5)
"""
topo [3, 1, 4, 2, 0]
0  ->  0
1  ->  5
2  ->  3
3  ->  8
4  ->  9
single source se har node ka shortest distance
by using DFS
if you want path then parent required
or backtrack kar ke path find kar sakte ho
"""
