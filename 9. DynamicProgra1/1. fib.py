"""
Q: Fibonacaii Series
   - 0, 1, 1, 2, 3, 5, 8, .....
   f(n) = f(n-1) + f(n-2) - Recursive relation
   f(0) = 0
   f(1) = 1

"""

# 1st step - write recursive sol - exponential TC


def Solve(n):
    # base case
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    """
    if n <= 1:
        return n
    ans = Solve(n - 1) + Solve(n - 2)
    return ans


# print(Solve(6))
# 2nd - step
# overlapping sub problems is there so apply DP
# overlapping subproblems computed again and again
# which DP to apply
# recursive function written in which parameters changes
# 1 parameter changes so 1-D DP eg, n changes
# jiten parameter ki value change ho gi wahi DP lagana HAII
# adding memoization - REC + MEMOIZATION
# Steps
# create DP array + pass in fun (Step-1) or Global create(bad habit)
# Store the ans in DP array (step-2)
# check if Dp array has alreay ans if yes than return, just after base cases(step-3)


def SolveMem(n, dp):
    # base case
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    """
    if n <= 1:
        return n
    # step-3
    if dp[n] != -1:
        # than answe is there
        return dp[n]
    ans = SolveMem(n - 1, dp) + SolveMem(n - 2, dp)
    # step -2
    dp[n] = ans
    return dp[n]


n = 10
# Step-1 create DP array and pass in func arg
# n - size DP passed so Index ERROR
# dp array of n-size - start index = 0, end_index = n-1
# Solve in accesing dp[n] which is not exists
# Increase size of DP as n+1
dp = [-1] * (n + 1)
print(SolveMem(10, dp))


"""
Bottom Up approch
step1: dp array creation
step2: base case analysis of recursive code and update dp array
step3: find the range of changing variables and copy paste the logic in rec code accordingly


"""


def SolveTab(nthTerm):
    # step 1 create dp array
    dp = [0] * (nthTerm + 1)
    # step 2 analyze base case and update dp array
    dp[0] = 0
    dp[1] = 1
    # step-3 range of changing variables
    # nthTerm goes till base case nthTerm -> 0 (top down)
    # 0 -> nthTerm botoom up - [2, nthTerm]
    for n in range(2, nthTerm + 1):
        # copy
        ans = dp[n - 1] + dp[n - 2]
        dp[n] = ans
    # what to return
    # nthTerm parameter pass so return dp[nthTerm]
    return dp[nthTerm]


print(SolveTab(10))


"""

Space optimization
dp ans dependes on which
[x,x,x]
current val depends on prev1, prev2

"""


def SolveTabOptim(nthTerm):
    prev2 = 0
    prev1 = 1
    curr = -1
    for n in range(2, nthTerm + 1):
        # copy
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1


print(SolveTabOptim(10))
