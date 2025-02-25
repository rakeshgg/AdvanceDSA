'''
Number Range

FINDING COUNT OF DUPLICATE NUMBERS IN A SORTED ARRAY

- Finding the first occurrence
- Finding the last occurrence

Thus, count of duplicate
elements = Index of the last occurrence - Index of the first occurrence + 1

arr = [1, 2, 2, 2, 2, 3, 4, 7 ,8 ,8]
k = 2, op = 4

'''


def find_count_of_dup_number(arr, k, is_first):
    start = 0
    end = len(arr) - 1
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if k == arr[mid]:
            ans = mid
            if is_first:
                end = mid - 1
            else:
                start = mid + 1
        elif k < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return ans


first_index = find_count_of_dup_number([1, 2, 2, 2, 2, 3, 4, 7, 8, 8], 2, True)
last_index = find_count_of_dup_number([1, 2, 2, 2, 2, 3, 4, 7, 8, 8], 2, False)
if first_index == -1 or last_index == -1:
    print(f"no valid number {first_index}")
else:
    dup_length = last_index - first_index + 1
    print(f"{dup_length}")
