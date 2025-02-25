'''
function complete_mission(mission, notebook)
   finish_mission(mission)
   notebook.write(mission)
   for each unlocked mission:
      if unlocked not in notebook
         complete_mission(unlocked) # dfs is recursive


function _dfs(graph, vertex, visited)
    visited.add(vertex) # help in back tracking if already visited
    for each neighbour in graph[vertex]:
        if neighbour not in visited:
           _dfs(neighbour)

'''


def _dfs(graph, vertex, visisted):
    print(vertex)
    visisted.add(vertex)
    for neighbour in graph.adj_list[vertex]:
        if neighbour not in visisted:
            _dfs(graph, neighbour, visisted)


def dfs(graph, vertex):
    visited = set()
    _dfs(graph, vertex, visited)


'''
if want to visit all vertex either graph connected or disconnected
- we need to apply dfs on every verex
and our code becomes

- Apply Dfs on all Vertex of Graph

def dfs(graph):
    visted = set()
    for vertex in graph:
       if vertex not visted:
          _dfs(graph, vertex, visited)

'''

'''
TC: Adjnacy List - Calls only one on vertex as visted set is there so once
Travesing each vertex  - v
Traversing dfs on each vertex - neighbours - degree(v) -

v + sum(deg(v))
v + 2E

O(v+E)

Adjnacy matrix - cost of travel each row for neighbours

O(V^2)
class stach size - O(V)

'''
