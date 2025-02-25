'''
https://leetcode.com/problems/valid-parentheses/
Valid paranthesis Problems
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

'''


def isValid(s):
    st = []
    for i in range(len(s)):
        ch = s[i]
        # opening bracket
        if ch in ["(", "{", "["]:
            # push in stack
            st.append(ch)
        else:
            # closing brackets
            # check opening haii ki nahi
            if len(st):
                topCh = st[-1]
                if ch == ')' and topCh == '(':
                    # match kar gya
                    st.pop()
                elif ch == '}' and topCh == '{':
                    # match kar gya
                    st.pop()
                elif ch == ']' and topCh == '[':
                    # match kar gya
                    st.pop()
                else:
                    # brackets not matching
                    return False
            else:
                return False
    if len(st):
        # if stack not empty
        return False
    else:
        # if stack empty
        return True


s = "()[]{}"
print(isValid(s))
