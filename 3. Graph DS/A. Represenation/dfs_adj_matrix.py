from adj_matrix import GraphAdjMat


def _dfs(graph, vertex, visisted):
    print(vertex)
    visisted.add(vertex)
    for neighbour in graph.get_neighbors(vertex):
        if neighbour not in visisted:
            _dfs(graph, neighbour, visisted)


def dfs(graph, vertex):
    visited = set()
    _dfs(graph, vertex, visited)


if __name__ == '__main__':
    graph = GraphAdjMat()
    graph.initialize(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
                     [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'E'), ('B', 'F'),
                      ('C', 'G'), ('D', 'H'), ('D', 'I')])
    print(*graph.adj_mat, sep='\n')
    dfs(graph, 'A')
