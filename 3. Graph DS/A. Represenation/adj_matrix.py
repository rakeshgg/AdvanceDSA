'''
Adjnacy matrix represenation for grpahs
Try to debug and understand this

'''


class GraphAdjMat:
    def __init__(self):
        # list of list - matrix
        self.adj_mat = []
        # map of character nodes to int nodes
        self.idx = {}
        # map of int nodes to character nodes
        self.label = {}

    def add_vertex(self, u):
        if u in self.idx:
            return
        for row in self.adj_mat:
            row.append(0)
        self.idx[u] = len(self.idx)
        self.label[len(self.label)] = u
        self.adj_mat.append([0]*(len(self.adj_mat)+1))

    def delete_vertex(self, u):
        if u not in self.idx:
            return
        self.adj_mat[self.idx[u]], self.adj_mat[-1] = self.adj_mat[-1], self.adj_mat[self.idx[u]]
        self.adj_mat.pop()
        for row in self.adj_mat:
            row[self.idx[u]], row[-1] = row[-1], row[self.idx[u]]
            row.pop()
        self.idx[self.label[len(self.adj_mat)]] = self.idx[u]
        self.label[self.idx[u]] = self.label[len(self.adj_mat)]
        del self.idx[u]
        del self.label[len(self.adj_mat)]

    def add_edge(self, u, v):
        if u not in self.idx:
            self.add_vertex(u)
        if v not in self.idx:
            self.add_vertex(v)
        self.adj_mat[self.idx[u]][self.idx[v]] = 1
        self.adj_mat[self.idx[v]][self.idx[u]] = 1

    def edge_exists(self, u, v):
        if u not in self.idx or v not in self.idx:
            return False
        return self.adj_mat[self.idx[u]][self.idx[v]] == 1

    def remove_edge(self, u, v):
        if u not in self.idx or v not in self.idx:
            return
        self.adj_mat[self.idx[u]][self.idx[v]] = 0
        self.adj_mat[self.idx[v]][self.idx[u]] = 0

    def get_vertices(self):
        return list(self.idx.keys())

    def get_neighbors(self, u):
        neighbors = []
        if u not in self.idx:
            return neighbors
        for v in self.label:
            if self.adj_mat[self.idx[u]][v] == 1:
                neighbors.append(self.label[v])
        return neighbors

    def initialize(self, vertices, edges):
        for u in vertices:
            self.add_vertex(u)
        for src, dest in edges:
            self.add_edge(src, dest)


if __name__ == '__main__':
    graph = GraphAdjMat()
    graph.initialize(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
                     [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'E'), ('B', 'F'),
                      ('C', 'G'), ('D', 'H'), ('D', 'I')])
    print(*graph.adj_mat, sep='\n')
    print(graph.idx)
    print(graph.label)
    print(graph.get_neighbors('A'))
    print(graph.edge_exists('A', 'B'))
    print(graph.edge_exists('A', 'E'))
    graph.remove_edge('A', 'B')
    print(graph.edge_exists('A', 'B'))
    graph.add_edge('A', 'B')
    print(graph.edge_exists('A', 'B'))
    graph.delete_vertex('A')
    print(*graph.adj_mat, sep='\n')
    print(graph.idx)
    print(graph.label)
