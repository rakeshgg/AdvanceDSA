'''
print string of char

'''


def tailRec(arr, i, n):
    if i == n:
        return
    print(arr[i])
    # Tail Recursion
    tailRec(arr, i+1, n)
    # No statement to execute


tailRec(['a', 'b', 'c'], 0, 3)
