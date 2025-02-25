'''
https://leetcode.com/problems/longest-valid-parentheses/
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')',
return the length of the longest valid (well-formed) parentheses
substring

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

soln: ans always -> even
- push -1 is stack -> calculating diff of indexes

- open - push index of start of stack
- close pop:
   - suppose valid expression for now
   - Find length
   - currentIndex - stacktopIndex

'''


def longestValidParentheses(s):
    st = []
    # for length find, invalid find
    # if brkt invalid it will help
    st.append(-1)
    maxLen = 0
    for i in range(len(s)):
        ch = s[i]
        if ch == '(':
            st.append(i)
        else:
            st.pop()
            # invalid bracket
            if len(st) == 0:
                # empty case
                # opening bracket nahi pada hoga
                # -1 popped out opening ki koi chij hi nahi tha
                # )))
                st.append(i)
            else:
                # valid bracket
                currLen = i - st[-1]
                maxLen = max(currLen, maxLen)
    return maxLen


s = ")()())"
print(longestValidParentheses(s))
