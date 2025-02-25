
def dfs(graph, vertex, visted, stack):
    visted.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visted:
            dfs(graph, neighbor, visted, stack)
    # push after all neighbours visted
    stack.append(vertex)


def topological_sort(graph):
    visited = set()
    stack = []
    for vertex in graph:
        if vertex not in visited:
            # calling for all unvisted vertex
            # similar to classic dfs
            dfs(graph, vertex, visited, stack)
    ordering = []
    while stack:
        # reversing the order
        ordering.append(stack.pop())
    return ordering

# what is graph has cycle - infinte loops -
# each vertex is waiting for other to end - mutual dependency
# if cycle(Back Edge than cycle) than toplogical sort is not possible
# if back edge is already in a path then we have a cycle
