'''
Word Break-2
140. Word Break II


Given a string s and a dictionary of strings wordDict, add spaces
in s to construct a sentence where each word is a valid dictionary
word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused
multiple times in the segmentation.


Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

Soln:


'''


def Solve(index, s, st, result, temp):
    # base case if cover all string
    if index >= len(s):
        # remove last space
        temp.strip()
        result.append(temp.strip())
        return
    # 1 case need to solve
    # helper str substrin to check
    sub_str = ''
    for i in range(index, len(s)):
        sub_str += s[i]
        if sub_str in st:
            Solve(i+1, s, st, result, temp + sub_str + " ")
            # if temp is global that is passed by refernce than backtracking is required


def wordBreak(s, wordDict):
    st = set()
    result = []
    st = set(wordDict)
    # start index = 0
    # temporary string
    temp = ''
    Solve(0, list(s), st, result, temp)
    return result


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(wordBreak(s, wordDict))
# op - ['cat sand dog', 'cats and dog']
