# n = size(nodes)

'''
def dfs(graph: Dict[int, List[int]], cur: int, visited: Set[int]):
    if cur in visited: return
    visited.add(cur)
    print(cur, end = " "); 
    for next in graph[cur]:
        dfs(graph, next, visited)


def bfs(graph: Dict[int, List[int]], node: int):
    q = deque([node])
    visited = set([node])
    while q:
        cur = q.popleft()     
        print(cur, end = " ")    
        for next in graph[cur]:
            if next in visited: 
                continue             
            q.append(next)
            visited.add(next)


'''