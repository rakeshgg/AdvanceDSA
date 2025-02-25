'''
375. Guess Number Higher or Lower II

We are playing the Guessing Game. The game will work as follows:

I pick a number between 1 and n.
You guess a number.
If you guess the right number, you win the game.
If you guess the wrong number, then I will tell you whether the number I
picked is higher or lower, and you will continue guessing.
Every time you guess a wrong number x, you will pay x dollars.
If you run out of money, you lose the game.
Given a particular n, return the minimum amount of money
you need to guarantee a win regardless of what number I pick.

Input: n = 10
Output: 16
Explanation: The winning strategy is as follows:
- The range is [1,10]. Guess 7.
    - If this is my number, your total is $0. Otherwise, you pay $7.
    - If my number is higher, the range is [8,10]. Guess 9.
        - If this is my number, your total is $7. Otherwise, you pay $9.
        - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 = $16.
        - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 = $16.
    - If my number is lower, the range is [1,6]. Guess 3.
        - If this is my number, your total is $7. Otherwise, you pay $3.
        - If my number is higher, the range is [4,6]. Guess 5.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.
            - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 = $15.
            - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 = $15.
        - If my number is lower, the range is [1,2]. Guess 1.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.
            - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 = $11.
The worst case in all these scenarios is that you pay $16. Hence, you only need $16 to guarantee a win.

Input: n = 1
Output: 0
Explanation: There is only one possible number, so you can guess 1 and not have to pay anything.

Example 3:

Input: n = 2
Output: 1
Explanation: There are two possible numbers, 1 and 2.
- Guess 1.
    - If this is my number, your total is $0. Otherwise, you pay $1.
    - If my number is higher, it must be 2. Guess 2. Your total is $1.
The worst case is that you pay $1.


player1 -> pick 1 number from 1 to n
player2 -> guess one number -> correct, incorrect
                               incorrect -> higher guess or lower guess
min money required to gurantee win
choose any of 1, 2, 3, ....., n
guess 1 => ans1
guess 2 => ans2

guess n => ansn
----------------
min(ans1, ...., ansn)

pattern:
mini = float('inf')
for i:start, end
    mini = min(mini, ..........?)
-> always worst case ans
-> if range shorter than guranteed ans
eg: 7 case gurnteed money to win
t is wrong
i is a wrogh choices than gurantedd ans is
ans(i) = i + max(f(start, i-1), f(i+1, end))

# Merge Interval Pattern


'''


def solve(start, end):
    # range end >= start
    # invalid range [5, 4]
    if start >= end:
        return 0
    mini = float('inf')
    for i in range(start, end+1):
        # choose i
        ans1 = solve(start, i-1)
        ans2 = solve(i+1, end)
        mini = min(mini, i + max(ans1, ans2))
    return mini


# top down
# start - 1 to n
# end - change i-1, n to 0
def solveMem(start, end, dp):
    if start >= end:
        return 0
    if dp[start][end] != -1:
        return dp[start][end]
    mini = float('inf')
    for i in range(start, end+1):
        ans1 = solve(start, i-1)
        ans2 = solve(i+1, end)
        mini = min(mini, i + max(ans1, ans2))
    dp[start][end] = mini
    return dp[start][end]


# bottom up
# start 1 to n, end n to 0 -> reverse this
def solveTab(n):
    dp = [[0]*(n+2) for _ in range(n+2)]
    for start in range(n, 0, -1):
        # if start > end no need to check so in above loop
        # of end start from start not from 1
        # start <= end so start+1 in range
        for end in range(start+1, n+1):
            mini = float('inf')
            for i in range(start, end+1):
                ans1 = dp[start][i-1]
                ans2 = dp[i+1][end]
                # i+1, accesign n+1 index index error
                mini = min(mini, i + max(ans1, ans2))
            dp[start][end] = mini
    return dp[1][n]


# space optimization possible
# i-1, i+1, current ans depends on n rows so its a 2d array


def getMoneyAmount(n):
    # dp = [[-1]*(n+1) for _ in range(n+1)]
    # return solve(1, n)
    # return solveMem(1, n, dp)
    return solveTab(n)


print(getMoneyAmount(10))
# 16
