'''
convert decimal to binary numbers

'''


def fun(n):
    if n == 0:
        return
    fun(n // 2)
    print(n % 2, end='')


fun(10)
