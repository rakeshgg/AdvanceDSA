'''
Given an integer n that represents the number of vertices,
labeled from 0 to n-1, an array edges of undirected edges,
a vertex start and a vertex end, we want to find the minimum
number of edges to go from start to end.

n = 6, edges = [[0, 1], [0, 2], [0, 3], [1, 2],
[1, 4], [2, 4], [3, 4], [3, 5], [4, 5]], start = 0, end = 5

output: 2

explanation: The minimum number of edges
required to go from 0 to 5 is 2, by taking the edge (0, 3) then the edge (3, 5).

if vertex == end
   return level
# that is min no of edges to reach to leaf

'''
from queue import Queue


def min_edges(n, edges, start, end):
    graph = [[] for _ in range(n)]
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)
    queue = Queue()
    visited = set()
    queue.put((start, 0))
    visited.add(start)
    while not queue.empty():
        vertex, level = queue.get()
        if vertex == end:
            return level
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                # level - level of actual vertex
                # unvisted is neighbour at next level so level+1
                queue.put((neighbor, level+1))
    return -1


if __name__ == '__main__':
    n: int = 6
    edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 4), (2, 4), (3, 4), (3, 5), (4, 5)]
    start = 0
    end = 5
    print(min_edges(n, edges, start, end))

    # Output:
    # 2
