import fibheap as fh


def reconstruct(prev, dest):
    path = [dest]
    while prev[dest]:
        dest = prev[dest]
        path.append(dest)
    return path[::-1]


def dijkstra(graph, src):
    dist = {}
    prev = {}
    # key is label of vertex, value is node objects
    nodes = {}
    queue = fh.makefheap()
    for u in graph:
        dist[u] = float('inf')
        prev[u] = None
        # insert in priority queue
        # (for comapring priority, to know node vertex when extracting)
        nodes[u] = fh.Node((dist[u], u))
        queue.insert(nodes[u])
    dist[src] = 0
    queue.decrease_key(nodes[src], (dist[src], src))
    while queue.minimum():
        u = queue.extract_min().key[1]
        # traverse neighbour
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                queue.decrease_key(nodes[v], (dist[v], v))
    return dist, prev

# why not used visted set
# because we are not reinserting visited set


if __name__ == '__main__':
    graph = {
        'A': [('B', 7), ('C', 10), ('E', 13), ('F', 14)],
        'B': [('D', 4), ('E', 8)],
        'C': [('F', 12), ('I', 22)],
        'D': [('E', 6), ('G', 15)],
        'E': [('G', 10), ('F', 7)],
        'F': [('G', 11), ('H', 13), ('I', 14)],
        'G': [('J', 12), ('H', 12)],
        'H': [('J', 6), ('K', 8), ('L', 9)],
        'I': [('H', 6), ('L', 8)],
        'J': [('K', 2)],
        'K': [('L', 10)],
        'L': []
    }
    src = 'A'
    dist, prev = dijkstra(graph, src)
    print(f'Shortest distances from {src} to vertices:')
    print(dist)
    dest = 'L'
    print(f'Shortest path from {src} to {dest}:')
    print(reconstruct(prev, dest))

    # Output:
    # Shortest distances from A to vertices:
    # {'A': 0, 'B': 7, 'C': 10, 'D': 11, 'E': 13, 'F': 14, 'G': 23, 'H': 27, 'I': 28, 'J': 33, 'K': 35, 'L': 36}
    # Shortest path from A to L:
    # ['A', 'F', 'H', 'L']
