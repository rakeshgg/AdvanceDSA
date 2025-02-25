"""
Graph-3
Topological Sort - Where apply topological sort

Q. no of components in Graph - BFS/DFS any, count ++ for every components
Q. number of Ilands 2D matrix given- find connected components
Q. Rotten Oranges - minimum time to rott all oranges just like burning tree
Q  Bridge in Graph - if remove edges than disconnected
           Har edge ko hata ke connected components count kar lo
Q. snake and ladder

Toplogical Sort:
- Linear ordering of vertices u comes before v in that ordering u -> v
- jiske pass dependecy nahi haii wahh pahle print karo
only applied on Topological Sort on -> DAG
can be done using BFS/DFS

- DFS -> jab kiski call se wapas ja raha hu then push to stack
      -> Role of Stack- Reverse order wise dependecy wise pushing
      (Reverse wise push)
         so on pop get right ans
      Apply simple DFS and on return store on Stack
      jiski dependency sabse kam haii wahh pahle ayega

- Using BFS, kahns algo is used
    -> jiski indegree 0 ho gi wahi queue me ayega
    -> indegree independent not depend on anyone
    -> The first vertex in topological sorting is always
    a vertex with an in-degree of 0 (a vertex with no incoming edges).
    -> if in queue than indegree zero so pahle se queue me hoga to visted nah
    use hota haii
    -> no need to visited as it can work for disconnected as well

# IMP
# cyclic graph - toplogical sort we cannot find all nodes beacuse
                 indegree zero nahi hota haii
                 cyclic graph me toplogical sort kavi complete nahi hota haii
                 cyclic graph me toplogical sort ka node ka length total number
                 of node ke equal nahi hota haii

"""

from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self):
        self.adjList = defaultdict(lambda: [])

    def addEdge(self, u, v, direction):
        self.adjList[u].append(v)
        if direction == 0:
            self.adjList[v].append(u)

    def printAdjaencyList(self):
        for key, value in self.adjList.items():
            print(key, " ->", value)

    def topoSortDFS(self, src, visited, stack):
        print(src, end=" -> ")
        visited[src] = True
        for neighbor in self.adjList[src]:
            if not visited.get(neighbor):
                self.topoSortDFS(neighbor, visited, stack)
        # while returing store in stack
        # store current node
        stack.append(src)

    def topoSortBFS(self, n, ans):
        # kahns algo
        # some issue on code
        # check 1:02
        q = deque()
        indegree = {}
        # initialize indegree to all nodes
        # no need to visited as it can work for disconnected as well
        for i in range(n):
            indegree[i] = 0
        # indegree calculation issue is here if
        # indegree is not initialized to zero first
        for i in self.adjList.items():
            print(i)
            # this become tuples, (2, [4, 5])
            _, nbrs = i[0], i[1]
            for nbr in nbrs:
                indegree[nbr] += 1
        # put all node inside queue whose indegree is zero
        print(indegree)
        # no need to visited as it can work for disconnected as well
        for i in range(n):
            if indegree.get(i) == 0:
                # push into the queue
                # pushed beause we want to delete that node
                q.append(i)
        # BFS Logic
        while len(q):
            fNode = q.popleft()
            print(fNode, "->", end="")
            ans.append(fNode)
            # if node popped than its indegree become less than 1
            # neighbor me ja ke indegree minus kar do
            # indegree adjustments
            for nbr in self.adjList[fNode]:
                indegree[nbr] -= 1
                # check for zero than again push to queue
                if indegree[nbr] == 0:
                    q.append(nbr)

    # directed graph me cyclic detect using BFS
    def topoSortBFSCycle(self, n):
        ans = []
        q = deque()
        indegree = {}
        for i in range(n):
            indegree[i] = 0
        for i in self.adjList.items():
            _, nbrs = i[0], i[1]
            for nbr in nbrs:
                indegree[nbr] += 1
        for i in range(n):
            if indegree.get(i) == 0:
                q.append(i)
        while len(q):
            fNode = q.pop()
            ans.append(fNode)
            for nbr in self.adjList[fNode]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)
        # cycle detection
        if len(ans) == n:
            print("valid top cycle not present")
        else:
            print("cycle present")


G = Graph()
G.addEdge(2, 1, 1)
G.addEdge(1, 2, 1)
G.addEdge(2, 3, 1)
G.addEdge(3, 4, 1)
G.addEdge(3, 5, 1)
G.addEdge(4, 6, 1)
G.addEdge(5, 6, 1)
G.addEdge(6, 7, 1)
# G.printAdjaencyList()
"""
n = 5
visited = defaultdict(lambda: False)
stack = []
for i in range(n):
    if not visited[i]:
        G.topoSortDFS(i, visited, stack)
print(stack)
while len(stack):
    print(stack.pop(), '->', end=' ')
"""
G = Graph()
G.addEdge(2, 4, 1)
G.addEdge(2, 5, 1)
G.addEdge(4, 6, 1)
G.addEdge(5, 3, 1)
G.addEdge(3, 7, 1)
G.addEdge(6, 7, 1)
G.addEdge(7, 0, 1)
G.addEdge(7, 1, 1)
G.printAdjaencyList()
ans = []
G.topoSortBFS(8, ans)
print("\n", ans)
# 2 ->4 ->5 ->6 ->3 ->7 ->0 ->1 ->
# multiple top sort can exits
