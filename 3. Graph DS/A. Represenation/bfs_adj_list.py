from adj_list import GraphAdjList
from queue import Queue


def _bfs(graph, vertex, visited):
    queue = Queue()
    queue.put(vertex)
    visited.add(vertex)
    while not queue.empty():
        vertex = queue.get()
        print(vertex)
        for neighbor in graph.adj_list[vertex]:
            if neighbor not in visited:
                queue.put(neighbor)
                visited.add(neighbor)


def bfs(graph):
    visited = set()
    for vertex in graph.get_vertices():
        if vertex not in visited:
            _bfs(graph, vertex, visited)


if __name__ == '__main__':
    graph = GraphAdjList()
    graph.adj_list = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'E', 'F'],
        'C': [],
        'D': ['H', 'I', 'J'],
        'E': ['B', 'K'],
        'F': ['B', 'L'],
        'H': ['D'],
        'I': ['D', 'O', 'J'],
        'J': ['D', 'I'],
        'K': ['E', 'P', 'L'],
        'L': ['K', 'Q', 'R', 'F'],
        'O': ['I'],
        'P': ['K'],
        'Q': ['L'],
        'R': ['L']
    }
    bfs(graph)
