'''
Given array sorted in ascending order
find elements k

mid = (start + end)//2 - overflow java, c, c++ etc
mid =  start + (end - start)//2 - avoid integer overflow condition


Move senario
compare mid with given elements k (Condition), decide to go to left or right
if go to left : end = mid - 1
if go to right: start = mid + 1

# condition
k == arr[mid] # found solution
k < arr[mid] # elements lie in left so mid - 1
k > arr[mid] # elemnts lie in right so mid + 1

# initialization
start = 0 # point to 1st elemnts on array
end = len(array) - 1 # point to end elements on array


# boundary condition
while start <= end
start and end both meet if 1 elemnts left in array - start == end is valid
start < end is also valid

'''


def binary_search(arr, k):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if k == arr[mid]:
            return mid
        elif k < arr[mid]:
            # smaller value lie in left
            end = mid - 1
        else:
            start = mid + 1
    return -1


print(binary_search([4, 6, 10], 10))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 2))
