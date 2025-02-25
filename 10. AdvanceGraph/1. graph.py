'''
Represenation of Graphs
Space - O(V*V)

'''


def adjMatrix(n, edges):
    adj = [[0]*n for _ in range(n)]
    for edge in edges:
        u, v = edge
        adj[u][v] = 1
    print(adj)
    # [[0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]]

# neighbors of adjmatrix
# how to find


# neigbour means 0 se kha kaha ja sakte ho
# neigbour means 1 se kha kaha ja sakte ho
# 0-1 ans 1-0 edge in undirected graph
'''
{
    0 : [1, 3],
    1:  [],
}
'''
n = 4
edges = [(0, 1), (0, 3), (1, 2), (2, 3)]
adjMatrix(n, edges)
