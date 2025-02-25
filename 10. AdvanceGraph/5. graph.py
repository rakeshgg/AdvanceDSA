"""
Directed Graph -> cycle detection
BFS -> Toplogical Sort required
DFS -> lets Do

same logic in BFS/DFS in undirected graph working
why not working here
-> Logic fail of Undirected cycle detection
-> node pe pahle kha se pauche ho ekbar parent set hogya than not set again
Logic:
Track rakhna padega recursion call stack ke andar kon kon
sa recursion call haii
kon kon sa hatt chuka hoga
let 5, 7, 8, in recursion call present
and agin 5 comes than cycle
cylic way me recursion present
tha cycle present

visted once true than not change again
dfs call stack :it can be changed
                if inside recursion stack than true
                if pop from recursion stack than false

"""

from collections import defaultdict

# from collections import deque


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

    def checkCyclicGraphUsingDFS(self, src, visited, dfsVisted):
        visited[src] = True
        dfsVisted[src] = True
        for nbr in self.adjList[src]:
            if not visited[nbr]:
                aageKaAns = self.checkCyclicGraphUsingDFS(nbr, visited, dfsVisted)
                if aageKaAns:
                    return True
            if visited[nbr] and dfsVisted[nbr]:
                return True
        # rec call chali gai pop ho gya
        # jab call aai to mark true kia
        # jab call wapas popout ho gya recursion stack se top wapas false kar dia
        # backtracking
        dfsVisted[src] = False
        return False


G = Graph()
G.addEdge(0, 1, 1)
G.addEdge(1, 2, 1)
G.addEdge(2, 3, 1)
G.addEdge(3, 4, 1)
G.addEdge(4, 0, 1)
G.printAdjaencyList()
n = 5
visited = defaultdict(lambda: False)
dfsVisted = defaultdict(lambda: False)
ans = False
for i in range(n):
    if not visited[i]:
        ans = G.checkCyclicGraphUsingDFS(i, visited, dfsVisted)
        if ans:
            break
if ans:
    print("cycle present")
else:
    print("no cycle")
