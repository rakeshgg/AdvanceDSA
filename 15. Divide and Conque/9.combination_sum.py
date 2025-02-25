'''
https://leetcode.com/problems/combination-sum/
39. Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations
of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations
that sum up to target is less than 150 combinations for the given input.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

soln:
pick/not-pick pattern

'''


def combinationSumHelper(candidates, target, v, ans, index):
    # base conditions
    if target == 0:
        # ans find
        ans.append(v[:])
    if target < 0:
        return
    for i in range(index, len(candidates)):
        # removing duplicates
        if i > index and (candidates[i] == candidates[i-1]):
            # than not pick
            continue
        v.append(candidates[i])
        # i+1 we are considering different elements
        # i same elemnts use again and again 
        combinationSumHelper(candidates, target-candidates[i], v, ans, i)
        # backtrack
        v.pop()


def combinationSum(candidates, target):
    ans = []
    v = []
    # ans is in sorted from so sorted
    candidates.sort()
    combinationSumHelper(candidates, target, v, ans, 0)
    print(ans)
    # ans have dupliacte entries
    # need to remove duplicate entries using set
    return ans


candidates = [2, 3, 5]
target = 8
combinationSum(candidates, target)
# check for part-6 lec buy sell stock
# [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
