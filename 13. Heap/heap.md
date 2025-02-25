# python in built collections

https://www.scaler.com/topics/heap-in-python/

# Heap

-> Complete Binary Tree
all levels are completely fill except last one
filling of node from left to right !.e Left is first filled than right fill
-> Follow heap property
-> Create in array Form but visualization in Tree Form

# Heap Property

max-heap : child se vada hu parent
min-heap: child se xota hu parent

if Indexing is from 1
Parent index -> i
left child -> 2i
right child -> 2i+1 = leftchild + 1
-> child to parent -> i/2

if Indexing is from 0
Parent index -> i
left child -> 2i + 1
right child -> 2i+ 2 = leftchild + 1

# Insertion on heaps

-> add node at the end of array
-> if not follow heap properties take it to right place
-> index is i, than its parent is i/2 and compare and go up
-> O(1) \* O(h) = O(logn)

# deletion

only root node can be deleted
delete root
copy last value ,,M,;P['.]
replace root with last value

-> root node ko correct position me paucha do
i -> 2i, 2i+1

insertion i -> i/2 ke taraf processing
deletion i -> 2i, 2i+1 ka processing
-> O(logn)

# heapify

- node ko sahi jagh paucha do
- any array can convert to heap using heapify
- node ka index dia hota haii
  heapify(arr, n, i)

# largest wala game

i -> 2i, 2i+1
find largest index and swap
loop ke alwa we can use recursion
-> postion left, right kar ke sahi jgh paucha doge

# Recursion -> heapify

# build heap - O(n)

-> leaf node ko heapify karne ki jarurat nahi haii !.e they are heap
-> (n/2 +1) to n are all leaf nodes
-> complete binary tree ke andar (n/2 +1) to n are Leaf Node
-> Remaning Tree (1 to n/2) is internal node need to heapify

# heap sort - nlogn

- swap 1st elements to last elements, so last one sorted
  -> heapify root
  -> continue
