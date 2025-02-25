'''
Minimum Brackets Reversal
- valid paranthesis, longest paranthesis solve than easier
Count the Reversal in - GeeksForGeeks
https://www.geeksforgeeks.org/problems/count-the-reversals0401/1

Given a string S consisting of only opening and closing curly
brackets '{' and '}', find out the minimum number of reversals
required to convert the string into a balanced expression.
A reversal means changing '{' to '}' or vice-versa.

Input:
S = "}{{}}{{{"
Output: 3
Explanation: One way to balance is:
"{{{}}{}}". There is no balanced sequence
that can be formed in lesser reversals.

Input:
S = "{{}{{{}{{}}{{"
Output: -1
Explanation: There's no way we can balance
this sequence of braces.

SOLN: switch perform open <-> close !.e Reversal to make it balance
(( -> Same char brackets: switch last one - reversal_count = 1 way
)( -> both diff char, -> both should be reverse -> reversal count = 2
() -> valid, reversal_count = 0

Valid Paranthesis Logic need to used
- I will remove valid pairs
- if stack is not empty than we will try to find reversal count
- if odd numbers char not possible to make pairs so no soln

'''


def countRev(s):
    # odd size string than impossible to make pairs
    if len(s) & 1:
        return -1
    ans = 0
    st = []
    for ch in s:
        if ch == '{':
            st.append(ch)
        else:
            # it will pe closing beackets
            if len(st) and st[-1] == '{':
                # pairup so pop
                st.pop()
            else:
                # no opening at top
                st.append(ch)
    # if stack still not Empty
    # let's count Reversal
    print(st)
    # ['}', '{', '{', '{']
    while len(st):
        a = st.pop()
        b = st.pop()
        if a == b:
            # {{
            # 1 reversal if same
            ans += 1
        else:
            # }{
            # if diff 2 reversal
            ans += 2
    return ans


s = "}{{}}{{{"
print(countRev(s))
# 3
