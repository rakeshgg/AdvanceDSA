"""
DP with Binary Search
Russian Dolls problems can also be solve using this approch

DP with Binary Search
i -> index -> jabtak increasing haii include
              agar nahi haii to new subsequnce start kar lo

Russian Dolls -> width, height
soln: how LIS lagg raha haii eha
curr elemnts piche se vada haii than include kar lunga
ek envelop purane wala ko apne andar fitt kar lega to LIS

Change in CODE comes at this points
arr[curr] > prev, curr width, height vada hona chaiie -
major change aata haii eha

eg: LIS with aboslute with diff in adjacent is exactly 1

def solve(arr, curr, prev):
    if curr >= len(arr):
        return 0
    include = 0
    if prev == -1 or arr[curr] > prev:
        include = 1 + solve(arr, curr+1, prev+1)
    exclude = 0 + solve(arr, curr+1, prev)
    ans = max(include, exclude)
    return ans


"""


"""
def solveOptimal(arr):
    if len(arr) == 0:
        return 0
    ans = []
    ans.append(arr[0])
    for i in range(len(arr)):
        if arr[i] > ans[-1]:
            # include
            ans.append(arr[i])
        else:
            # overiride
            # find index of just bada number
            # ans arr ke andar arr[i] ka lower bound de do
            # check this lower_bound
            index = lower_bound(ans, arr[i])
            ans[index] = arr[i]
    return len(ans)
"""
