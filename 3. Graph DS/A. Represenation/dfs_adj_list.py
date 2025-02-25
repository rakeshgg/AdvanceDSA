

from adj_list import GraphAdjList


def _dfs(graph, vertex, visisted):
    print(vertex)
    visisted.add(vertex)
    for neighbour in graph.adj_list[vertex]:
        if neighbour not in visisted:
            _dfs(graph, neighbour, visisted)


def dfs(graph, vertex):
    visited = set()
    _dfs(graph, vertex, visited)


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
    dfs(graph, 'A')
