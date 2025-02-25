'''
Next Letter Problems
find next letter which comes after k -
similar to Ceil problems but if equals return next elemnts

'''


def search_next_letter(arr, k):
    n = len(arr)
    # next letter is required
    if k < arr[0] or k > arr[n-1]:
        return arr[0]
    start = 0
    end = n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if k == arr[mid]:
            # return next letter
            start = mid + 1
        elif k < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    # since at end mid + 1 is out of bound start = end + 1
    # so % n is applied to make it circular
    return arr[start % n]


print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
