"""
cycle detection in directed graph/undirected Graph
using BFS, DFS
BFS - level wise traversal

Undirected Graph -> Find Cycle
Cycle using BFS -> Queue
    Pattern: Node which is already visited and not parent than cycle
            Agar koi node pahle se visited haii (iss node pe pahle tum
            pauch chuke ho)
            tum dubara uss node pe pauch gye to check parent gya uss node pe
            ya koi dusra gya
            koi node agar already visted haii to uska parent ne visted karwaya hoga
            abb dubara uss node pe pauch chuke ho agr wahi parent dubara wahi tak
            paucha to koi dikkat nahi but if different node se same node pe pauch
            paye to than cycle
    cyclic graph haii to from different parent you can reach to same node
    kisi node pe aye hoge to parents se hi aye hoge

BFS:

two path to reach to same node beacuse of cycle
started from two different path and colliding to some points that is beacus of cycle.
When you come to node from two differnt parents than its a cycle

IF someone visited and it didnot come from it than its not parent
# check connected comonents

different parents se same node and visited

"""

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
            print(key, " ->", value)

    def bfs(self, src, visited):
        # TC -> O(E+V)
        q = deque()
        q.append(src)
        visited[src] = True
        while len(q):
            frontNode = q.popleft()
            # ans
            print(frontNode, "->", end=" ")
            # insert neighbors
            for neighbour in self.adjList[frontNode]:
                if not visited.get(neighbour):
                    # new node addd in queue and mark it as visited
                    q.append(neighbour)
                    visited[neighbour] = True

    def checkCyclicUsingBFS(self, src, visited):
        q = deque()
        parent = {}
        q.append(src)
        parent[src] = -1
        visited[src] = True
        while len(q):
            frontNode = q.popleft()
            for nbr in self.adjList[frontNode]:
                if not visited[nbr]:
                    q.append(nbr)
                    visited[nbr] = True
                    # parent se hi neighbor pe hi ayega
                    parent[nbr] = frontNode
                else:
                    # already visited and jis node
                    # se aa rahe ho wahh parent nahi haii
                    # than cycle
                    # {0: -1, 1: 0, 4: 0, 3: 4} 4 0
                    print(parent, frontNode, nbr)
                    # if nbr is visited and its not its own parents
                    # than coming to nbr from differnt parents again
                    if frontNode != parent[nbr]:
                        return True
        return False

    def checkCyclicUsingDFS(self, src, visited, parent):
        visited[src] = True
        for nbr in self.adjList[src]:
            if not visited[nbr]:
                checkAageKaAns = self.checkCyclicUsingDFS(nbr, visited, src)
                if checkAageKaAns:
                    # cycle found
                    return True
            # nbr is visted and parents are differnt
            if visited[nbr] and nbr != parent:
                # cycle present
                print(nbr, parent)
                return True
        return False


G = Graph()
G.addEdge(0, 1, 0)
G.addEdge(1, 2, 0)
G.addEdge(2, 3, 0)
G.addEdge(3, 4, 0)
G.addEdge(4, 0, 0)
G.printAdjaencyList()
n = 5
ans = False
visited = defaultdict(lambda: False)
# use to find the connected components
for i in range(n):
    if not visited[i]:
        # ans = G.checkCyclicUsingBFS(i, visited)
        ans = G.checkCyclicUsingDFS(i, visited, -1)
        if ans:
            break
if ans:
    print("cycle is present")
else:
    print("not cyccle")
