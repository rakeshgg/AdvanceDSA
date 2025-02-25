'''
Head recursion

'''


def headRec(arr, i, n):
    if i == n:
        return
    # head Recursion
    headRec(arr, i+1, n)
    # printing operation happes while retuning
    print(arr[i])


headRec(['a', 'b', 'c'], 0, 3)
# op - cba
