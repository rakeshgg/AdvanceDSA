'''
find sum of natural numbers
SUM(N) = N + N-1 + N-2 + ......... + 1

Recursive Fn is - fun(n-1)

Recursive Call  n + fun(n-1)
Base case: N = 1

'''


def sum(n):
    if n == 1:
        return n
    return n + sum(n-1)


print(sum(10))
