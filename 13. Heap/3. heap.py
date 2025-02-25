'''
Heap in Python

heapq

-> by default, the heap will always be a min heap

functions:

heapify: converts an iterable into a heap data structure, in-place
heappush: inserts an element into a heap, and after insertion,
         the order is adjusted accordingly so that the heap structure is maintained

heappop: removes and returns the smallest element of the heap, and after removal,
         the order is adjusted accordingly

heappushpop: This function can push and pop elements into the heap. This function
             first pushes the provided element* to the heap and then pops the smallest
             element from the heap

nlargest: This function returns the k-largest elements from the heap
nsmallest: This function returns the k-smallest elements from the heap

# explore in object formats also
https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python

'''

# Creating a Heap in Python
import heapq
# Initialize arr
arr = [9, 7, 2, 8, 6]
heapq.heapify(arr)
print(arr)
# [2, 6, 9, 8, 7]


# Inserting into Heap
arr.append(1)
print(arr)
# [2, 6, 9, 8, 7, 1]
# append elemnts at last index
# Heapify the array again
heapq.heapify(arr)
print(arr)
# [1, 6, 2, 8, 7, 9]


'''
since you are using Python, you don't have to append elements and heapify
the whole array again and again. We will be using the help push function
to insert elements into the heap.heappush function inserts an element into
the heap and heapifies it.

'''
# Initialize arr
arr = [9, 7, 2, 8, 6]

# Use heapify to convert arr into a heap
heapq.heapify(arr)

# Push elements into the heap
heapq.heappush(arr, 1)
print(arr)
# [1, 6, 2, 8, 7, 9]

'''
Removing Element From the Heap in Python

heappop function to remove the element from the heap.
heappop function removes and returns the smallest element
from the heap, which means it always removes the element at the first index.

'''
# Initialize arr
arr = [9, 7, 2, 8, 6]

# Use heapify to convert arr into a heap
heapq.heapify(arr)

# Pop element from the heap
popEle = heapq.heappop(arr)

# Print the popped element
print(popEle)
# 2

# Print the heap after removing an element
print(arr)
# [6, 7, 9, 8]


# Replacing an element in a Heap in Python
# Initialize arr
arr = [9, 7, 2, 8, 6]

# Use heapify to convert arr into a heap
heapq.heapify(arr)
print(arr)

# Replace the smallest element of the heap with the given element
heapq.heapreplace(arr, 10)
print(arr)


# Using Heap to Find the Largest and the Smallest Element
# Initialize arr
arr = [9, 7, 2, 8, 6, 3, 5, 4]

# Use heapify to convert arr into a heap
heapq.heapify(arr)

print(heapq.nlargest(2, arr))
print(heapq.nsmallest(2, arr))


# Max Heap
# max heap means the largest element will always be at the 0th index.
# To implement max heap, just multiply every element by -1. By doing this,
# the largest element will become the smallest element, and it will come at the front.
# Initialize arr
arr = [3, 2, 6, 8, 7]

# Add a minus sign to all the elements of the array
arr = list(map(lambda x: -x, arr))

# Use heapify to convert arr into a heap
heapq.heapify(arr)

print(arr)
# [-8, -7, -6, -2, -3]
