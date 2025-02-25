# path to check back edges - Loop(Cycle)

def dfs(graph, vertex, visted, stack, path):
    visted.add(vertex)
    path.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour in path or (neighbour not in visted and not dfs(graph, neighbour, visted, stack, path)):
            return False
    stack.append(vertex)
    # remove from path beacuse we are about to backtrack
    path.remove(vertex)
    return True


def topological_sort(graph):
    visited = set()
    path = set()
    stack = []
    for vertex in graph:
        if vertex not in visited:
            # calling for all unvisted vertex
            # similar to classic dfs
            if not dfs(graph, vertex, visited, stack, path):
                return []
    ordering = []
    while stack:
        # reversing the order
        ordering.append(stack.pop())
    return ordering

# detect cycle


def has_cycle(graph):
    ordering = topological_sort(graph)
    return len(graph) > 0 and len(ordering) == 0

# tc - V + E
# sc - V


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

    print(topological_sort(graph))
    # Output: [13, 2, 5, 4, 8, 11, 1, 0, 3, 6, 9, 7, 10, 14, 12]
