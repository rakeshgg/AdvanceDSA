'''
modulo using recursion


'''


def mod(num, den):
    if num < den:
        return num
    return mod(num-den, den)


print(mod(10, 4))
