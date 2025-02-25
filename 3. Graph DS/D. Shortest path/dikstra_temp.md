Templates


def dijkstra(graph, src)
    dist <- {}
    open <- list()
    # this need to rember infinity to all node 0 to source
    for u in graph:
       dist[u] <- infinite
       open.add(u)
    # shortest distance to reach source
    dist[src] <- 0
    while not open.empty():
       u <- extract u from open with smallest dist[u]
       # traverse u neighbours
       for v, w in graph[u]:
         if dist[u] + w < dist[v]:
            # best path edge relaxation
            dist[v] <- dist[u] + w
    return dist

# shortest distance from source
how to find actual path 
- keep track of previous vertex of each
vertex every time we update to v we also update its previous vertex
- keep going backward from prev table 
path A to L

we start from L 
Prev[l] is h
prev[h] is f
prev[f] is A
prev[A] is None, we stop
reverse the path



def dijkstra(graph, src)
    dist <- {}
    prev <- {} # for tracking of path
    open <- list()
    # this need to rember infinity to all node 0 to source
    for u in graph:
       dist[u] <- infinite
       prev[u] <- None, we dont know so null
       open.add(u)
    # shortest distance to reach source
    dist[src] <- 0
    while not open.empty():
       u <- extract u from open with smallest dist[u]
       # traverse u neighbours
       for v, w in graph[u]:
         if dist[u] + w < dist[v]:
            # best path edge relaxation
            dist[v] <- dist[u] + w
            prev[v] <- u
    return dist, prev


def reconstruct(prev, dest)
    path <- [dest]
    vertex <- dest
    while prev[vertex] is not None:
       vertex <- prev[vertex]
       path.append(vertex)
    return path.reversed()


            

What datastucture to choose

- dist/prev - Hash table
- open - extract vertex from open with smallest distance
       - using array 
          - v iteration each extract min
            vertex which can of v(degree of u) - v^2
          - use priority queue with sorted array - O(E * V)
          - Heap - max-heap, min-heap (Binary Heap) - (E + V)*log(v)
          - Fibnocai Heap - (E + V*Log(V))
          





