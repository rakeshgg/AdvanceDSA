'''
Permutation of Strings
str = 'abc', print all permutaion
i - position
j - is char tak swap karn haii

'''


def printPermutation(str_arr, i):
    # base case
    if i >= len(str_arr):
        print(''.join(str_arr))
        return
    # swapping i, j
    for j in range(i, len(str_arr)):
        str_arr[i], str_arr[j] = str_arr[j], str_arr[i]
        # recursive calls
        printPermutation(str_arr, i+1)
        # backtracking to recreate orginl input or state
        str_arr[i], str_arr[j] = str_arr[j], str_arr[i]


if __name__ == '__main__':
    str = "abc"
    i = 0
    printPermutation(list(str), i)
    # print(ans)
    '''
    ans wit backtracking
    abc
    acb
    bac
    bca
    cba
    cab
    ans with out backtracking which is wrong
    abc
    acb
    cab
    cba
    abc
    acb
    '''
