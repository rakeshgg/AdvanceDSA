'''
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

1047. Remove All Adjacent Duplicates In String

You are given a string s consisting of lowercase English letters. A duplicate removal
consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.
It can be proven that the answer is unique.

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters
are adjacent and equal, and this is the only possible move.
The result of this move is that the string is "aaca", of which
only "aa" is possible, so the final string is "ca".
Example 2:
Input: s = "azxxzy"
Output: "ay"

SOLN: using Stack
String - in place removal is not possible
Push into stack -> when second char match with s.top than remove
                -> pairing kar raha hu
                -> ans return in reverse


'''


def removeDuplicates(s):
    st = []
    for ch in s:
        if len(st) and st[-1] == ch:
            # pairup means pop
            # adjacent same char ko remove kar dia
            st.pop()
        else:
            st.append(ch)
    # no need to reverse in python print stack as array
    # you can treat it as stack and pop till empty
    return ''.join(st)


print(removeDuplicates("azxxzy"))
