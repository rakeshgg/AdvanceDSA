'''
count number of Vowels

'''


def is_Vowle(str):
    if str in ['a', 'e', 'i', 'o', 'u']:
        return 1
    return 0


def CountVowel(str):
    if str == '':
        return 0
    if is_Vowle(str[0]):
        return 1 + CountVowel(str[1:])
    else:
        return CountVowel(str[1:])


print(CountVowel('aeirkz'))
