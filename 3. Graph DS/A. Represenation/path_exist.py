'''
input
n=9
edges = [[0,1],[0,2],[2,4],[3,5],[5,6],[5,7],[6,8]]
start=0
end=6
output=False
Explanation
6 is not rechable from 0

'''


def dfs(graph, vertex, end, visited):
    # base cases if visted end one than path
    if vertex == end:
        return True
    visited.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            if dfs(graph, neighbour, end, visited):
                return True
    return False


def path_exists(n, edges, start, end):
    # insted of adj list lets use adj matrix
    graph = [[] for _ in range(n)]
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)
    visited = set()
    return dfs(graph, start, end, visited)
    # initially visited is empty
    # every time visted we add in that
    # so if all are visted than path is there else not
    # return end in visited


# n+m
if __name__ == '__main__':
    n = 9
    edges = [[0, 1], [0, 2], [2, 4], [3, 5], [5, 6], [5, 7], [6, 8]]

    start = 0
    end = 6
    print(f'Path exists from {start} to {end}: {path_exists(n, edges, start, end)}')

    start = 3
    end = 6
    print(f'Path exists from {start} to {end}: {path_exists(n, edges, start, end)}')

    # Output:
    # False
    # True
