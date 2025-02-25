'''
Decode String
https://leetcode.com/problems/decode-string/

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string
inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no
extra white spaces, square brackets are well-formed, etc. Furthermore,
you may assume that the original data does not contain any digits and
that digits are only for those repeat numbers, k. For example, there will
not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

SOLN: 3[a2[bc]]
  -> First decode internal than external -> similar to brackets matching
  -> Inner to Outer Solve kar ke ana haii
  chr -> actual string
  numeric ->
  a2[bc] -> decode first and push in stack

'''


def decodeString(s):
    '''
    s = '123789'
    print(s.isdigit())
    Python isdigit() returns True only
    if the string consists of all digit
    characters with no alphabets
    '''
    # stack
    st = []
    for ch in s:
        if ch == ']':
            stringToRep = ""
            while len(st) and not st[-1].isdigit():
                # pop till digit founds
                stringToRep += st.pop()
            # need to revers
            stringToRep = stringToRep[::-1]
            numericTimes = ""
            while len(st) and st[-1].isdigit():
                numericTimes += st.pop()
            # "321" -> how to convert in integers
            # reverse numeric types
            numericTimes = numericTimes[::-1]
            n = int(numericTimes)
            # final decoding
            currentDecode = stringToRep * n
            print(currentDecode)
            st.append(currentDecode)
        elif ch != '[':
            # ignore opening brackets
            st.append(str(ch))
    ans = ''.join(st)
    return ans


s = "2[abc]3[cd]ef"
print(decodeString(s))
# abcabccdcdcdef
