'''
Print n to 1

'''

# Iterative


def Iteration(n):
    while n >= 1:
        print(n)
        n -= 1


def recursion(n):
    if n < 1:
        return
    print(n)
    recursion(n-1)


Iteration(5)
recursion(5)
