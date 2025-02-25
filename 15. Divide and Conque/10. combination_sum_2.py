'''
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target
number (target), find all unique combinations in candidates where
the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

SOLN:
- Ek bar use karna haii candiadate ko
- duplicate combination no allowded
2, 5, 2, 1, 2
target = 5
- (1, 2, 2)

'''


def combinationSumHelper(candidates, target, v, ans, index):
    # base conditions
    if target == 0:
        # ans find
        ans.append(v[:])
    if target < 0:
        return
    for i in range(index, len(candidates)):
        v.append(candidates[i])
        # i is given because we are considering smae elements again and again
        # i+1 we are considering different elements
        # i same elemnts use again and again 
        combinationSumHelper(candidates, target-candidates[i], v, ans, i+1)
        # backtrack
        v.pop()


def combinationSum2(candidates, target):
    ans = []
    v = []
    candidates.sort()
    combinationSumHelper(candidates, target, v, ans, 0)
    print(ans)


# [[1, 2, 5], [1, 7], [1, 6, 1], [2, 6], [2, 1, 5], [7, 1]] -- op if i+1


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
combinationSum2(candidates, target)