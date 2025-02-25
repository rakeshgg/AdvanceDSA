'''
Adjaency List
d = defaultdict(lambda:[]), #{0:[]}

avg -> Space - O(V+E)
Worst -> spce -> O(V*V)

'''

from collections import defaultdict


class Graph:
    # 0 ke corresponding neighbors store karna haii
    def __init__(self):
        self.adjList = defaultdict(lambda: [])

    def addEdge(self, u, v, direction):
        # source u
        # destination v
        # direction -> directed=1
        # undeirected=1
        # create an edge from u to v
        self.adjList[u].append(v)
        if direction == 0:
            # undireced edge
            # create and edge from v to u
            self.adjList[v].append(u)

    def addEdgeWeight(self, u, v, weight, direction):
        # create an edge from u to v
        self.adjList[u].append((v, weight))
        if direction == 0:
            # create and edge from v to u
            self.adjList[v].append((u, weight))

    def printAdjaencyList(self):
        for key, value in self.adjList.items():
            print(key, ' ->', value)


G = Graph()
G.addEdge(0, 1, 0)
G.addEdge(1, 2, 0)
G.addEdge(0, 2, 0)
G.printAdjaencyList()
G = Graph()
G.addEdgeWeight(0, 1, 4, 0)
G.addEdgeWeight(1, 2, 5, 0)
G.addEdgeWeight(0, 2, 9, 0)
G.printAdjaencyList()
