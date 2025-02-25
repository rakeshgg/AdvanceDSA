'''
Indirect Recursion

globl - acess as global varibale
nonlocal - acess it as local scope

'''

n = 1


def even():
    global n
    if n == 10:
        return
    print(f'even - {n}')
    n += 1
    odd()


def odd():
    global n
    if n == 10:
        return
    print(f'odd - {n}')
    n += 1
    even()


odd()
