'''
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

dependes on execution of next rec calls  - n * fact(n-1)
optimization using Tail recursion

fact(5) = 5 * fact(4)
fact(4) = 5 * 4 * fact(3)
fact(3) = 5 * 4 * 3 * fact(2)
fact(2) = 5 * 4 * 3 * 2 * fact(1)

dependency
n * fact(n-1) depends on return value of next recursive call we need to eliminate that
fact(n-1)

send as argument as fact(n-1, n * ans)
which will take result of factorial


'''


def fact(n, ans):
    if n <= 1:
        return ans
    # tail Recursive calls
    # compiler optimized to make loops
    return fact(n-1, ans * n)


print(fact(5, 1))
