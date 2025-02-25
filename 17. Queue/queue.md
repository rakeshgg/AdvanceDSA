
# Methods Available in Queue
- put(item):The queue provides the put(item) method in python
            to insert an element into the queue.
- get():The get() method uses the front pointer to get an element of the queue.
- empty():The queue is empty if the empty() method returns true.
          Else, the queue has some elements in it.
- qsize():The qsize() method is provided by the queue in
           python to get the size, i.e., the number of elements
           present in the queue.
- full(): The full() method is vice versa of the empty() method.
          The full() method is provided by the queue in python to
          check whether the queue is full or not

# Implementation of Queue in Python
   We can implement a queue in python using a list. The list is a built-in linear data structure present in python. For inserting and deleting an element from the list queue, we need to shift the entire elements present in the queue(list). Hence, the list implementation is slower as the inserting and deleting elements take O(N) time.

   NOTE: If we are implementing a queue using a list, then the append() method is used in place of the enqueue() method, and the pop() method is used in place of the dequeue() method.

   ## 1. Initializing a list-based queue 
   queue = []
   # Enqueue elements or appending elements
   queue.append(1)
   queue.append(2)
   print(queue)
   # Dequeue elements or popping elements
   print(queue.pop(0))
   print(queue.pop(0))
   print(queue)

   ## 2.Implementation using collections.deque   ---> Use this always
   One of the advantages of using the collection module is that appending
   and deleting elements takes a constant amount of time i.e., O(1)
   time complexity only.
   in place of enqueue() -> append()
   in place of dequeue() ->  popleft()

    from collections import deque
    # Initializing a class-based dequeue queue 
    queue = deque()
    
    # Enqueue elements or appending elements
    queue.append(1)
    queue.append(2)

    print(queue)
    
    # Dequeue elements or popping elements
    print(queue.popleft())
    print(queue.popleft())
    print(queue)

# Implementation using queue.Queue
    In python, we have a module called Queue. We can also implement
    the queue in python using the Queue module.
    One of the advantages of using the Queue module is that we can initialize an infinite-sized queue. To initialize an infinite queue, we can set the maxsize variable to 0. For example: Queue(maxsize = 0).
    from queue import Queue
    # Initializing a Queue module based queue with size = 2
    q = Queue(maxsize = 2)
    # qsize() give the maxsize
    # of the Queue
    print(q.qsize())
    # Enqueue elements putting elements
    q.put(1)
    q.put(2)
    print("Size of the queue: ", q.qsize())
    # Dequeue elements or getting elements
    print(q.get())
    print(q.get())
    print("Size of the queue: ", q.qsize())

