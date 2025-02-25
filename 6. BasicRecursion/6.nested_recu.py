'''
Nested Recursion

'''


def fun(n):
    if n > 10:
        return n-1
    return fun((fun(n+2)))


print(fun(5))
