'''
Celebrety Problems
https://www.geeksforgeeks.org/the-celebrity-problem/

In a party of N people, only one person is known to everyone.
Such a person may be present at the party, if yes, (s)he doesn't
know anyone at the party. We can only ask questions like “does A know B? “.
Find the stranger (celebrity) in the minimum number of questions.
We can describe the problem input as an array of numbers/characters
representing persons in the party. We also have a hypothetical function
HaveAcquaintance(A, B) which returns true if A knows B, and false otherwise.
How can we solve the problem?

Input:
MATRIX = { {0, 0, 1, 0}, {0, 0, 1, 0}, {0, 0, 0, 0}, {0, 0, 1, 0} }
Output: id = 2
Explanation: The person with ID 2 does not know anyone but everyone knows him

Input:
MATRIX = { {0, 0, 1, 0}, {0, 0, 1, 0}, {0, 1, 0, 0}, {0, 0, 1, 0} }
Output: No celebrity
Explanation: There is no celebrity.

SOLN:
BruteForce: if celibrity -> row all zeros
            and if celibrity all knows HIM -> all 1's (all knows celibrity)
        -> check rows and cols of each person from 0 to n [0, n)
           both condition fulfill or not -> TC:O(N^2)

# optimization:
   - Put all person in stack
   - while stack size is 1
      pick person top two say A, B
      check if A ->B ko jana haii if yes
      Than A is not celibrety
      discard A
      and B ko push kar denge
      else:
        B, A ko janta haii to B celibrety nahi haii
        B is dicarded, Push A
    - That single person in stack might be a celibrety
      lets verify using row, col iteration
'''


def celebrity(M, n):
    # stack
    st = []
    # step1, push all person into stack
    for i in range(n):
        st.append(i)
    # step2, run discard method to get might be celeberity
    print(st)
    # [0, 1, 2, 3]
    while len(st) != 1:
        a = st.pop()
        b = st.pop()
        # if a knows b
        if M[a][b]:
            # a is not celebrity b might be
            st.append(b)
        else:
            # b is not celebrity a might be
            st.append(a)
    # step-3, check that single person is actually celebrity
    print(st)
    # [2]
    mightBeCeleribty = st.pop()
    # cell should not know any one -> roww all zeros
    for i in range(n):
        if M[mightBeCeleribty][i] != 0:
            return -1
    # Every should Know celebrity
    for i in range(n):
        # diagonal elemnts xodd ke sara zero nahi hona chaiie
        if (M[i][mightBeCeleribty] == 0) and (i != mightBeCeleribty):
            return -1
    return mightBeCeleribty


M = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
n = len(M)
Celebrity = celebrity(M, n)
print(Celebrity)
