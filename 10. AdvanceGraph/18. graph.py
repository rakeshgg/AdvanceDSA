'''
Floyd Warshall -> all source shortest path

'''

from collections import defaultdict


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
            print(key, ' ->', value)

    def floydWarshal(self, n):
        # create 2D array
        dist = [[float('inf')]*n for _ in range(n)]
        # mark zero on diagonals
        for i in range(n):
            dist[i][i] = 0
        # distnaces availbe in graph insert and update dist
        # graph ke according distance update
        for t, nbrs in self.adjList.items():
            u = t
            for nbr in nbrs:
                v, wt = nbr
                dist[u][v] = wt
        for helper in range(n):
            for src in range(n):
                for dest in range(n):
                    # depend on previous state so its dp
                    dist[src][dest] = min(dist[src][dest], dist[src][helper] + dist[helper][dest])
        print(dist)


G = Graph()
G.addEdgeWeight(0, 1, 3, 1)
G.addEdgeWeight(0, 3, 5, 1)
G.addEdgeWeight(1, 0, 2, 1)

G.addEdgeWeight(1, 3, 4, 1)
G.addEdgeWeight(2, 1, 1, 1)
G.addEdgeWeight(3, 2, 2, 1)

# G.addEdgeWeight(3, 2, 5, 1)
# G.addEdgeWeight(4, 3, -3, 1)

G.printAdjaencyList()
print("\n")
src = 0
# no of node
n = 4
G.floydWarshal(n)
# [[0, 3, 7, 5], [2, 0, 6, 4], [3, 1, 0, 5], [5, 3, 2, 0]]
