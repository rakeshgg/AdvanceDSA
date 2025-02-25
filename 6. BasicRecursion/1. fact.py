'''
Factorial using Recursion
fact(6) = 6 * 5 * 4 * 3 * 2 * 1
fact(N) = N * (N -1) * (N-2) * .........1
Recursive call = N * fun(N-1)
Base case : N == 1


'''


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)


print(fact(5))
