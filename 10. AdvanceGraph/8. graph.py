"""
Disktra algo -> 1:19

Algorithums -> Heap/minheap -> min elemnts in O(1)
               or set -> no duplicate store in sorted order in c++
               Greedy approch
               distance array

Refer -> https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/

"""

from collections import defaultdict
import heapq


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

    def shortestDistDisktra(self, src, n):
        # store distnace of node
        dist = defaultdict(lambda: float("inf"))
        pq = [(0, src)]
        while len(pq) > 0:
            # get smallest elemnts from heap
            current_distance, current_vertex = heapq.heappop(pq)
            # Nodes can get added to the priority queue multiple times. We only
            # process a vertex the first time we remove it from the
            # priority queue.
            if current_distance > dist[current_vertex]:
                continue
            # traverse the neighbour
            for nbr in self.adjList[current_vertex]:
                # check distance can be updated or not
                distance = current_distance + nbr[1]
                if distance < dist[nbr[0]]:
                    # Only consider this new path if it's better than any
                    # path we've
                    # already found.
                    # distance update karna haii in heap and dist map also
                    dist[nbr[0]] = distance
                    heapq.heappush(pq, (distance, nbr[0]))
        print("\n")
        print(dist.values())


G = Graph()
G.addEdgeWeight(6, 3, 2, 1)
G.addEdgeWeight(6, 1, 14, 1)
G.addEdgeWeight(3, 1, 9, 1)
G.addEdgeWeight(3, 2, 10, 1)
G.addEdgeWeight(1, 2, 7, 1)
G.addEdgeWeight(2, 4, 15, 1)
G.addEdgeWeight(3, 4, 11, 1)
G.addEdgeWeight(6, 5, 9, 1)
G.addEdgeWeight(5, 4, 6, 1)
G.printAdjaencyList()
print("\n")
src = 6
# no of node
n = 7
G.shortestDistDisktra(src, n)
