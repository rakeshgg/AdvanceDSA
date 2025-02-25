'''
How to represent graph on Memeory
vertex - have unique id say integer/string(series)
        /class of people(name, age salary)
Edge - source and destination two vertex its connect

 or using tupe of 2 elements - (src, des)
class Edges:
   def __init__(self, src, dest):
       self.src = src
       self.dest = dest
# weighted grpah
or using tupe of 2 elements - (src, des, weight)
class Edges:
   def __init__(self, src, dest, weight):
       self.src = src
       self.dest = dest
       self.weight = weight

Adjnacy List
verex -> [] # neighbours vertex

using array - key is as index - 0 -> [2, 3, 4] - what if key is string?
Hash table - keys is any hasable type


'''


class GraphAdjList:

    def __init__(self):
        # hash table to vertex to array of vertices
        self.adj_list = {}

    def add_vertex(self, u):
        if u not in self.adj_list:
            self.adj_list[u] = []

    def remove_vertex(self, u):
        if u not in self.adj_list:
            return
        # deleted vertex and its edges from dict
        del self.adj_list[u]
        # delete u from all other vertex which is act as Edges
        for v in self.adj_list:
            if u in self.adj_list[v]:
                # removing from adj list
                self.adj_list[v].remove(u)

    def add_edge(self, u, v):
        # adding vertex
        if u not in self.adj_list:
            self.add_vertex(u)
        if v not in self.adj_list:
            self.add_vertex(v)
        # adding Edges if undirected graph
        # u -> v, v-> u
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        # if direced than only u -> v
        # if weighted add with weight (u, w), (v, w)

    def remove_edge(self, u, v):
        # undirected graph
        if (u in self.adj_list and v in self.adj_list[u]) \
               and (v in self.adj_list and u in self.adj_list[v]):
            self.adj_list[u].remove(v)
            self.adj_list[v].remove(u)

    def edge_exists(self, u, v):
        return u in self.adj_list and v in self.adj_list[u]

    def get_vertices(self):
        return self.adj_list.keys()

    def get_neighbors(self, u):
        if u not in self.adj_list:
            return []
        return self.adj_list[u]

    def initialize(self, verices, edges):
        for u in verices:
            self.add_vertex(u)
        for src, des in edges:
            self.add_edge(src, des)


if __name__ == '__main__':
    graph = GraphAdjList()
    graph.initialize(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
                     [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'E'), ('B', 'F'),
                      ('C', 'G'), ('D', 'H'), ('D', 'I')])
    print(graph.adj_list)
    print(graph.get_neighbors('A'))
    print(graph.edge_exists('A', 'B'))
    print(graph.edge_exists('A', 'E'))
    graph.remove_edge('A', 'B')
    print(graph.edge_exists('A', 'B'))
    graph.add_edge('A', 'B')
    print(graph.edge_exists('A', 'B'))
    graph.remove_vertex('A')
    print(graph.adj_list)

'''
{
        'A': ['B', 'C', 'D'],
        'B': ['A', 'E', 'F'],
        'C': ['A', 'G'],
        'D': ['A', 'H', 'I'],
        'E': ['B'],
        'F': ['B'],
        'G': ['C'],
        'H': ['D'],
        'I': ['D']
    }

    ['B', 'C', 'D']

    True

    False

    False

    True
    {
        'B': ['E', 'F'],
        'C': ['G'],
        'D': ['H', 'I'],
        'E': ['B'],
        'F': ['B'],
        'G': ['C'],
        'H': ['D'],
        'I': ['D']
    }

'''
