'''
Find string length using recursion

'''


def StringLength(str):
    if str == "":
        return 0
    return 1 + StringLength(str[1:])


print(StringLength('abc'))
