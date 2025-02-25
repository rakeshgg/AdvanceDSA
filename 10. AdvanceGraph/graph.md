Graph is a data stucture Nodes -> vertex, 
                                  Edges - connect nodes

Directed/Undirected Graph
Degree
Indegree/Outdegree
path
cyclic graph
acyclic graph

Adjancy Matrix
Adjancy List -- Majorly used


Adjancy matrix
number of nodes = 4
make 4*4 2D matrix
2d = [[0]*nodes for _ in range(nodes)]
2d = [[0] * coloums for _ in range(rows)]
nodes = 0, 1, 2, 3 -> 4*4 maatrix
0->1 edges - true/false !.e 0 or 1



from collections import deque
append()
appendleft()
pop()
popleft()

# Stack
s = deque()
s.append(1);  # 1
s.append(2);  # 1,2
s.append(3);  # 1,2,3
s.pop();      # 1,2
s.pop();      # 1


# Queue
q = deque()
q.append(1);  # 1
q.append(2);  # 1,2
q.append(3);  # 1,2,3
q.popleft();  # 2,3
q.popleft();  # 3


# LinkedList
ll = deque() 
ll.append(1);     # 1
ll.append(2);     # 1,2
ll.appendleft(0); # 0,1,2
ll.pop();         # 0,1
ll.popleft();     # 1

len(dequeue)


from collections import defaultdict
def_value -> should be callable !.e function
d = defaultdict(def_value)
# list of dictionary
# lambda is callable 
d = defaultdict(lambda:[]), #{0:[]}
d = defaultdict(lambda:0), by default zero if no values


# Traveral
BFS -> Level order Traveral
DFS -> preorder, postorder, inorder(Recursion)
