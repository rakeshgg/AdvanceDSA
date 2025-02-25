'''
https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
Minimum Number of Coins

arr = [1, 2, 3]
target = 7
min number of elements you have to take to reach target sum

prev question given only a, b, c
here array given may be any size
- every elemnts of array have gone through recursive call

target ->  at last you got 0
2 - way -> if Zero found at leaf than target formed,
           send max if zero than update
           (length=0 send from root and add 1 every call)
        -> return karwa do if leaf 1 + kar ke vej do root pe

'''


def minCoin(target, arr):
    # her number ko minus kar rahe haii
    if target == 0:
        return 0
    if target < 0:
        # Invalid ans
        # min no of ans in INT MAX
        return float('inf')
    # recursive call
    mini = float('inf')
    for i in range(len(arr)):
        # we need to find minimum
        # if ans not found in any cases
        # ans = min(ans, minCoin(target-arr[i], arr))
        ans = minCoin(target-arr[i], arr)
        # able to make target
        # jis elemnts pe hu waha se call marunga
        # har call se ans ayega jo invalid aur valid hoga
        # invalid ans inf
        if ans != float('inf'):
            # 1 + beacuse one elemnts used so 1 + kar ke upar vej rahe haii
            mini = min(mini, 1 + ans)
    return mini


# traget chnage - array same - 1D - DP
# traget n to 0
def minCoinMem(target, arr, dp):
    if target == 0:
        return 0
    if target < 0:
        return float('inf')
    if dp[target] != -1:
        return dp[target]
    mini = float('inf')
    for i in range(len(arr)):
        ans = minCoinMem(target-arr[i], arr, dp)
        if ans != float('inf'):
            mini = min(mini, 1 + ans)
    dp[target] = mini
    return dp[target]


# Bottom-UP Dp Convert
def minCoinTab(t, arr):
    # min ans nikalana haii so initialize with int max
    dp = [float('inf')]*(t+1)
    dp[0] = 0
    # range of target - [0, t]
    for target in range(1, t+1):
        mini = float('inf')
        for i in range(len(arr)):
            # this becomes -ve target-arr[i] also
            if target-arr[i] >= 0:
                ans = dp[target-arr[i]]
                if ans != float('inf'):
                    mini = min(mini, 1 + ans)
        dp[target] = mini
    # jo recursive call me vejte haii - t
    return dp[t]


# dp target depends on mini
# mini depends on ans
# ans depends on dp[target-arr[i]]
# dp[t] --> dp[t- arr[i]], arr[i] can be anything
# dp[7] depends on all of array so space optimization not possible
# can it solve in O(1) space any other Method


arr = [1, 2, 3]
target = 7
# print(minCoin(target, arr))
# op - 3
# dp = [-1] * (target+1)
# print(minCoinMem(target, arr, dp))
print(minCoinTab(target, arr))
