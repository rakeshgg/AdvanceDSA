'''
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all
possible letter combinations that the number
could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Solution:
# DE SHAW, ARCESIUM
mapping in phone number
map - 2 -> abc
3 - def
4 - ghi
5 - jkl
6 - mno
7 - pqrs
8 - tuv
9 - wxyz

ip - 2
char - abc - choices - > a, b, c

ip - 23
2 -> a, b, c
3 -> d, e, f

Similar to -> include patern, har char ko kyse include karenge using loops
- Include char
- Recursive
- exclude char, backtracking


'''


def solve(ans, index, output, digits, mapping):
    # base case
    if index >= len(digits):
        ans.append(''.join(output))
        return
    # 1 case solve baki
    digitInteger = int(digits[index])
    value = mapping[digitInteger]
    for i in range(len(value)):
        ch = value[i]
        # include ch
        output.append(ch)
        solve(ans, index+1, output, digits, mapping)
        # backtrack
        output.pop()


def letterCombinations(digits):
    # empty string handling
    if len(digits) == 0:
        return []
    ans = []
    index = 0
    output = []
    mapping = {}
    mapping[2] = "abc"
    mapping[3] = "def"
    mapping[4] = "ghi"
    mapping[5] = "jkl"
    mapping[6] = "mno"
    mapping[7] = "pqrs"
    mapping[8] = "tuv"
    mapping[9] = "wxyz"
    solve(ans, index, output, digits, mapping)
    print(ans)


letterCombinations("23")
# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
