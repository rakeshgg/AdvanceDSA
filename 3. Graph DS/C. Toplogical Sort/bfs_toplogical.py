from collections import defaultdict
from queue import Queue
'''
More Intutive - kahan's algorithums
count indegree of each vertex
indegree with 0 has no prerequistic can start from them
removing vertex from Queue and decrese indegree

'''
'''
count indegree of each vertex
queue <- Queue having indegree[u] == 0
while not queue.empty()
    vertex - queue.pop()
    ordering.add(vertex)
    check its outgoing neighbours
    for each neighbor in vertex:
       indegree[neighbor] -= 1
       if indegree[neighbor] == 0:
          queue.push(neighbor)
'''


def toplogical_sort(graph):
    # count in degree
    # creating default 0 for indegree
    # adjancy list
    # visted set not required used when adding same vertex multiple time
    # each vertex is added to queue exactly once if indegree is 0
    indegree = defaultdict(lambda: 0)
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    queue = Queue()
    # adding indegree 0 in queue
    for vertex in graph:
        if indegree[vertex] == 0:
            queue.put(vertex)
    ordering = []
    while not queue.empty():
        vertex = queue.get()
        ordering.append(vertex)
        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.put(neighbor)
    # if cycle inderdepency - nothing queue
    if len(ordering) < len(graph):
        return []
    return ordering


if __name__ == '__main__':
    graph = {
        0: [3, 6],
        1: [3],
        2: [4, 5],
        3: [6, 7],
        4: [3, 7, 8],
        5: [4, 8],
        6: [7, 9],
        7: [10],
        8: [11],
        9: [10, 12],
        10: [12, 14],
        11: [14],
        12: [],
        13: [14],
        14: []
    }

    print(toplogical_sort(graph))
    # Output: [0, 1, 2, 13, 5, 4, 3, 8, 6, 11, 7, 9, 10, 12, 14]
