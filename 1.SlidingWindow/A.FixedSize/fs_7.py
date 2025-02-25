'''
maximum of all subarry of size k
or
minimum of all subarray of size k
of
find max of all minimum of subarray of size k

'''
# maximum of all subarray of size k


def max_of_every_ws_k(arr, k):
    ans = []
    min_item = float('-inf')
    i, j = 0, 0
    # act as queue
    max_items = [min_item]
    print(max_items)
    while j < len(arr):
        # do calculation for j
        # store elements in queue which can be maximum in future
        # elements less then(no use in future) j elements
        # less than j can be used in future
        while len(max_items) and max_items[-1] < arr[j]:
            max_items.pop()
        max_items.append(arr[j])
        window_size = j - i + 1
        if window_size < k:
            j += 1
        elif window_size == k:
            # ans will be in front of list
            if len(max_items):
                ans.append(max_items[0])
                # removing calculation of i
                if max_items[0] == arr[i]:
                    max_items.pop(0)
            else:
                ans.append(0)
            i += 1
            j += 1
    return ans


print(max_of_every_ws_k([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(max_of_every_ws_k([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))
