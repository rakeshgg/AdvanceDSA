from adj_matrix import GraphAdjMat
from queue import Queue


def _bfs(graph, vertex, visited):
    queue = Queue()
    queue.put(vertex)
    visited.add(vertex)
    while not queue.empty():
        vertex = queue.get()
        print(vertex)
        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                queue.put(neighbor)
                visited.add(neighbor)


def bfs(graph):
    visited = set()
    for vertex in graph.get_vertices():
        if vertex not in visited:
            _bfs(graph, vertex, visited)


if __name__ == '__main__':
    graph = GraphAdjMat()
    graph.initialize(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
                     [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'E'), ('B', 'F'),
                      ('C', 'G'), ('D', 'H'), ('D', 'I')])
    print(*graph.adj_mat, sep='\n')
    bfs(graph)
