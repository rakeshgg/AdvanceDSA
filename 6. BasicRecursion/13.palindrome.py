'''

check palindrome or not

'''


def isPalindrome(str, start, end):
    if start >= end:
        return 1
    if str[start] == str[end]:
        return isPalindrome(str, start + 1, end - 1)
    else:
        return 0


print(isPalindrome('acca', 0, 3))
