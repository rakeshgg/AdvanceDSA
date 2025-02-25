'''
1st -ve in Every Window size k

'''


def first_neg_number_every_ws_k(arr, k):
    ans = []
    i, j = 0, 0
    # used as queue
    neg_num = []
    while j < len(arr):
        # do calulcation for j
        if arr[j] < 0:
            neg_num.append(arr[j])
        window_size = j - i + 1
        if window_size < k:
            j += 1
        elif window_size == k:
            # if no -ve number then append its as zero
            if len(neg_num) == 0:
                ans.append(0)
            else:
                ans.append(neg_num[0])
                # pop only if match with arr[i]
                if neg_num[0] == arr[i]:
                    neg_num.pop(0)
            i += 1
            j += 1
    return ans


print(first_neg_number_every_ws_k([12, -1, -7, 8, -15, 30, 16, 28], 3))
print(first_neg_number_every_ws_k([-2, 5, 1, 8, -2, 9, -1], 2))
