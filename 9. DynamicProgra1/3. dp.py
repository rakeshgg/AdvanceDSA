'''
https://www.geeksforgeeks.org
/maximise-number-of-cuts-in-a-rod-if-it-can-be-cut-only-in-given-3-sizes/
given rod with n length
can cut in 3 size A, B, C
Find maximum number of cuts
if 0 cut's than -1 ans
a = 10
b = 11
c = 3
n = 17
                                 length remaning
nlenth - 3 option - utilize A -> n-A
                    utilize B -> n-B
                    utilize C -> n-C
ek case hum solve karenge baki recursion

Fibonacaii pattern - 2 Recursive call
Inclusion Exclusion

   (1) - ans - intmin
   / | \
  Intmin
-> Bottom up approch - check initialization part its tough

'''


def solve(n, a, b, c):
    # at last n is zero than ans found
    if n == 0:
        # return 1
        return 0
    # length is negative
    # if no cuts
    if n < 0:
        # return 0
        # ans not allowed
        # return -1
        # answer hi nahi bann sakta
        # minimum
        return float('-inf')
    maxi = float('-inf')
    # recursive call
    first = solve(n-a, a, b, c)
    second = solve(n-b, a, b, c)
    third = solve(n-c, a, b, c)
    # we want maximum ans
    # why 1 is added beacuse we needd to count number of cuts
    # on return travelling up the tree count number of branches
    # this will give 1 more ans
    # so to fix let fix base case n == 0 return 0, n<0 -1, float('-inf')
    maxi = max(maxi, 1 + max(first, second, third))
    return maxi


# only n changes no change in other variables so 1-DP
# n is going till zero
# adding memoization
def solveMEM(n, a, b, c, dp):
    if n == 0:
        return 0
    if n < 0:
        return float('-inf')
    if dp[n] != -1:
        return dp[n]
    first = solveMEM(n-a, a, b, c, dp)
    second = solveMEM(n-b, a, b, c, dp)
    third = solveMEM(n-c, a, b, c, dp)
    ans = 1 + max(first, second, third)
    dp[n] = ans
    return ans


n = 17
a = 10
b = 11
c = 3
# ans = solve(n, a, b, c)
# dp = [-1] * n
# size should make it n+1, other wise index error
# index is from 0 to n
# because accesing n+1 above
dp = [-1] * (n+1)
ans = solveMEM(n, a, b, c, dp)
# if not possible to cut than ans is -1
if ans < 0:
    ans = -1
print(ans)
# op -3
