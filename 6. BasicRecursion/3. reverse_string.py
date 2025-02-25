'''
Reverse String

'''


def reverseString(arr, n):
    for i in range(0, n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
        # using ~ operation
        # use in two pointer approch to swap values
        '''
        ~i ===> -(i+1)
        x = 0, ~x = -1  -(i+1)
        x = 1, ~x = -2
        x = 2, ~x = -3
        Remember that negative numbers are stored as the two's
        complement of the positive counterpart. As an example,
        here's the representation of -2 in two's complement: (8 bits)
        The complement operator (~) JUST FLIPS BITS. It is up to
        the machine to interpret these bits.
        arr[i], arr[~i] = arr[~i] , arr[i]
        '''
    return arr


def reverseRecursion(arr, i, n):
    if i == n // 2:
        return
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    # loop
    reverseRecursion(arr, i+1, n)


def reverseString_(str):
    if str == "":
        return ""
    return reverseString_(str[1:]) + str[0]


arr = ['a', 'b', 'c', 'd', 'e']
n = len(arr)
reverseString(arr, n)
print(arr)
arr = ['a', 'b', 'c', 'd', 'e']
n = len(arr)
reverseRecursion(arr, 0, n)
print(arr)
print(reverseString_('abcde'))

# Note in python string is immutable
# so use split - list and join ans
