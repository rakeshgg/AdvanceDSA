'''
BFS -> level first, -> burn tree, neighbors first at same level
    -> Queue

DFS -> depth -> Recursion

'''

from collections import defaultdict
from collections import deque


class Graph:
    # 0 ke corresponding neighbors store karna haii
    def __init__(self):
        self.adjList = defaultdict(lambda: [])

    def addEdge(self, u, v, direction):
        self.adjList[u].append(v)
        if direction == 0:
            self.adjList[v].append(u)

    def printAdjaencyList(self):
        for key, value in self.adjList.items():
            print(key, ' ->', value)

    def bfs(self, src):
        # TC -> O(E+V)
        q = deque()
        visited = {}
        q.append(src)
        visited[src] = True
        while len(q):
            # pop from front of the queue
            frontNode = q.popleft()
            # ans
            print(frontNode, '->', end=' ')
            # insert neighbors
            for neighbour in self.adjList[frontNode]:
                if not visited.get(neighbour):
                    # new node addd in queue and mark it as visited
                    q.append(neighbour)
                    visited[neighbour] = True

    def extendedbfs(self, src, visited):
        # TC -> O(E+V)
        q = deque()
        q.append(src)
        visited[src] = True
        while len(q):
            frontNode = q.popleft()
            # ans
            print(frontNode, '->', end=' ')
            # insert neighbors
            for neighbour in self.adjList[frontNode]:
                if not visited.get(neighbour):
                    # new node addd in queue and mark it as visited
                    q.append(neighbour)
                    visited[neighbour] = True

    def dfs(self, src, visited):
        # take neighbors based on choices
        # simple recursion
        # dfs(0), call print, mark visited
        # neighbor pe recursive call
        print(src, end=' -> ')
        visited[src] = True
        for neighbor in self.adjList[src]:
            if not visited.get(neighbor):
                self.dfs(neighbor, visited)


G = Graph()
G.addEdge(0, 1, 0)
G.addEdge(1, 2, 0)
G.addEdge(1, 3, 0)
G.addEdge(3, 5, 0)
G.addEdge(3, 7, 0)
G.addEdge(7, 6, 0)
G.addEdge(7, 4, 0)
G.printAdjaencyList()
# G.bfs(0)
# if graph G have multple compnents
# than how to handle it
# if n = 8, node -> 0, 7
# range 8 -> 0 to 7
# run loop for all nodes
# disconnected components
visited = {}
for i in range(8):
    # har node ko source mann ke karenege
    # TC - same as visted than not possible to again
    if not visited.get(i):
        G.extendedbfs(i, visited)
# print('\n', visited)
print('\n')
# dfs can also have diconnected components
visited = {}
for i in range(8):
    # har node ko source mann ke karenege
    # TC - same as visted than not possible to again
    if not visited.get(i):
        G.dfs(i, visited)
# print('\n', visited)
