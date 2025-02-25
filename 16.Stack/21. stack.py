'''
https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

1003. Check If Word Is Valid After Substitutions

Given a string s, determine if it is valid.

A string s is valid if, starting with an empty string t = "",
you can transform t into s after performing the following operation any number of times:

Insert string "abc" into any position in t. More formally, t becomes
tleft + "abc" + tright, where t == tleft + tright. Note that tleft and tright may be empty.
Return true if s is a valid string, otherwise, return false.

Example 1:

Input: s = "aabcbc"
Output: true
Explanation:
"" -> "abc" -> "aabcbc"
Thus, "aabcbc" is valid.
Example 2:

Input: s = "abcabcababcc"
Output: true
Explanation:
"" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
Thus, "abcabcababcc" is valid.

SOLN:
t -> tleft, tright
SOLN-> Using Recursion
Ulta chalenge s -> t banyenge (empty string)

# Optimization -> in one iteration
pattern if valid -> har bar abc ka pair najar ayega
-> abcabcababcc
break kar ke bich me abc dal rahe ho
Pirup-> stack -> abab  got c, pop a,b
last stack empty ans = True else False

'''


def isValid(s):
    '''
    If the substring is present in the string,
    find() returns the index, or the character
    position, of the first occurrence of the
    specified substring from that given string.

    If the substring you are searching for is not present
    in the string, then find() will return -1
    TC -> O(n^2)
    find, left, right -> 3 * O(n)
    Recursive call-> tabtk none nahi hota
    Recursive call -> number of abc ->n/3
    3*n*n/3 => O(N^2)

    '''
    # if empty string than
    if len(s) == 0:
        return True
    fnd = s.find("abc")
    if fnd != -1:
        # found string
        tleft = s[0:fnd]
        tright = s[fnd+3:len(s)]
        return isValid(tleft+tright)
    return False


def isValidOptimized(s):
    # a top pe haii tavi b push hoga
    # ba, ca not pushed
    # pairup
    # sc -> O(n)
    # TC -> O(n)
    if s[0] != 'a':
        return False
    # stack
    st = []
    for ch in s:
        if ch == 'a':
            st.append(ch)
        elif ch == 'b':
            if len(st) and st[-1] == 'a':
                st.append(ch)
            else:
                return False
        else:
            # ch == 'c'
            if len(st) and st[-1] == 'b':
                # pair found
                st.pop()
                # check stack empty or not
                if len(st) and st[-1] == 'a':
                    st.pop()
                else:
                    return False
            else:
                return False
    return len(st) == 0


# print(isValid("aabcbc"))
print(isValidOptimized("abcabc"))
