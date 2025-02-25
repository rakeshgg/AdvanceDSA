'''
Allocate Minimum Number of Pages

1. Atleat 1 book allocated to every one
2. continous allocation only allowded

number of pages number line (sorted) - apply binary search
min = 0, max = sum of all pages - range where mid need to be
search and minimized

in our case min one book need to given to each students
range max(arr) and sum(arr)

if sechema not work go to right increse pages
if schema work go to left and minimize it

'''


def is_valid(arr, s, mid):
    # allocating books to students
    # mid is threshold max pages we can assign to 1 students
    # s is total number of students
    # greedy Approch - choose optimal
    student = 1
    total_sum = 0
    for each_book in arr:
        total_sum += each_book
        if total_sum > mid:
            # added one student with mid number pf pages
            student += 1
            total_sum = each_book
        if student > s:
            return False
    return True


def AllocateBooks(arr, s):
    # number of students s
    n = len(arr)
    if n < s:
        return -1
    start = max(arr)
    end = sum(arr)
    res = -1
    while start <= end:
        mid = (start + end) // 2
        if is_valid(arr, s, mid):
            # this can be a possible ans
            res = mid
            # minimize the number of pages
            end = mid - 1
        else:
            # maximize number of pages
            start = mid + 1
    return res


print(f'{AllocateBooks([12, 34, 67, 90], 2)}')
print(f'{AllocateBooks([5, 17, 100, 11], 4)}')
