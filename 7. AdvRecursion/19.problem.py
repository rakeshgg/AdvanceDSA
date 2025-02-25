'''
72. Edit distance

Given two strings word1 and word2,
return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')


Match or not match pattern
Horse - ros
i       j
match or not match
match - word[i] == word[j], call age i++, j++
not match
  c1. insert
  c2. replace
  c3. delete
  min(c1, c2, c3)

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u'

'''


def solve(word1, word2, i, j):
    # word is small than insert that one
    if i == len(word1):
        return len(word2) - j
    if j == len(word2):
        return len(word1) - i
    # id match
    if word1[i] == word2[j]:
        return solve(word1, word2, i+1, j+1)
    else:
        # no match
        # insert i same postion j+1
        insertAns = solve(word1, word2, i, j+1)
        # replace h - r
        # i++, j++
        replaceAns = solve(word1, word2, i+1, j+1)
        # h delete - i++, j remain same
        deleteAns = solve(word1, word2, i+1, j)
        # +1 why adding operations for match so added
        final_ans = min(insertAns, replaceAns, deleteAns) + 1
        return final_ans


def minDistance(word1, word2):
    return solve(word1, word2, 0, 0)


print(minDistance("horse", "ros"))
# 3
