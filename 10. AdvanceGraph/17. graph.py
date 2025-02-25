'''
Disktra -> Fails in -Ve Cycle, beacuse every cycle it give minimum so BellmanFord
        -> +ve cycle it can apply

BellmanFord Algo

-> -Ve Cycle detection
-> also find minimum

n - nodes
Relaxation -> total n-1 times
you get all shortest path

why Relaxation, why n-1 times
Relaxation:
source node dist + dist current node < dist[v]
than update this is relaxation and need to do
n-1 times

-VE Cycle Detection: infinite pass updation continue
- Relaxation on Edges
- detect cycle run rleaxation one more time if distance get updated than -ve cycle

TC -> O(N*V)

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

    def bellmanFordAlgo(self, src, n):
        # assuming directed weighted graph
        dist = [float('inf')] * n
        dist[src] = 0
        # n-1 relaxation steps
        for i in range(n-1):
            # for all Edges
            for e, nbrs in self.adjList.items():
                u = e
                for nbr in nbrs:
                    v, wt = nbr
                    if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                        dist[v] = dist[u] + wt
        # to check -ve cycle run rlaxation steps one more times
        negativeCycle = False
        for e, nbrs in self.adjList.items():
            u = e
            for nbr in nbrs:
                v, wt = nbr
                if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
                    negativeCycle = True
                    print(negativeCycle)
                    break
        if negativeCycle:
            print("Negative cycle present")
        else:
            print("negative cycle not present")
        print(dist)


G = Graph()
G.addEdgeWeight(0, 1, -1, 1)
G.addEdgeWeight(0, 2, 4, 1)
G.addEdgeWeight(1, 2, 3, 1)

G.addEdgeWeight(1, 3, 2, 1)
G.addEdgeWeight(1, 4, 2, 1)
G.addEdgeWeight(3, 1, 1, 1)

G.addEdgeWeight(3, 2, 5, 1)
G.addEdgeWeight(4, 3, -3, 1)

G.printAdjaencyList()
print("\n")
src = 0
# no of node
n = 5
G.bellmanFordAlgo(src, n)
# [0, -1, 2, -2, 1]
