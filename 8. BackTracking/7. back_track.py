'''
Given n pairs of parentheses, write a function
to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

# soln
- every position open or closed - 2 calls like include, exclude
- first character is always open one always gurantee(any expression may open bracket 1st)
-
open = 3, closed = 3
remaing_open = 0
remaning_closed = 0
output
temp: where result need to build

Valid Combinations:
current_open == n and
current_close == n

remaning_open == 0 and
remaning_closed == 0

'''


def solve(temp, currOpen, currClose, remOpen, remClose, res):
    if remOpen == 0 and remClose == 0:
        res.append(temp)
        return
    # open bracket wali recursive call
    # if open bracket use then it should be present
    if remOpen > 0:
        oldTemp = temp
        temp += '('
        # added one open brackets
        solve(temp, currOpen+1, currClose, remOpen-1, remClose, res)
        # backtrack wapas aa rha hu than want to remove
        temp = oldTemp
    # closed bracket wali recursive call
    if remClose > 0 and currOpen > currClose:
        oldTemp = temp
        temp += ')'
        solve(temp, currOpen, currClose+1, remOpen, remClose-1, res)
        # back track
        temp = oldTemp


def generateParenthesis(n):
    # start from
    temp = '('
    currOpen = 1
    currClose = 0
    remOpen = n-1
    remClose = n
    result = []
    solve(temp, currOpen, currClose, remOpen, remClose, result)
    return result


print(generateParenthesis(3))
# op - ['((()))', '(()())', '(())()', '()(())', '()()()']
