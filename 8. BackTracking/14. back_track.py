'''
1723. Find Minimum Time to Finish All Jobs
You are given an integer array jobs, where jobs[i]
is the amount of time it takes to complete the ith job.

There are k workers that you can assign jobs to.
Each job should be assigned to exactly one worker.
The working time of a worker is the sum of the time
it takes to complete all jobs assigned to them. Your
goal is to devise an optimal assignment such that
the maximum working time of any worker is minimized.

Return the minimum possible maximum working time of any assignment.

Example 1:

Input: jobs = [3,2,3], k = 3
Output: 3
Explanation: By assigning each person one job, the maximum time is 3.
Example 2:

Input: jobs = [1,2,4,7,8], k = 2
Output: 11
Explanation: Assign the jobs the following way:
Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
Worker 2: 4, 7 (working time = 4 + 7 = 11)
The maximum working time is 11.

SOLn:
This Problem is solved using binary search
Range -> ans and mimimize the range to find
possible ans
eg:Book allocation problems
  painter problems
  Aggregasive Cow


- Job assignments to workers
- can have multiple assignments - get min among them
- sare arragements nikal lo and find ans - min
- every i index should assign to all workers from 1 to k
- solve - index pe solve karo
- Optimization:
# Recursion tree


class Solution:
    def minimumTimeRequired(self, jobs, k):
        if k == len(jobs):
            return max(jobs)
        self.min_val = float("inf")

        def backtrack(idx,ans):
            if idx == len(jobs):
                self.min_val = min(self.min_val,max(ans))
                return
            seen = set()
            for i in range(k):
                if ans[i] in seen: continue
                if ans[i] + jobs[idx] >= self.min_val: continue
                seen.add(ans[i])

                ans[i] += jobs[idx]
                backtrack(idx+1,ans)
                ans[i] -= jobs[idx]

        backtrack(0,[0]*k)
        return self.min_val


'''

finalAns = float('inf')


def Solve(i, k, n, jobs, work, ans):
    # base case if i is out of array
    global finalAns
    if i == n:
        ans = max(work)
        finalAns = min(finalAns, ans)
        return
    # optimization
    # at any point max work is grater than old ans
    if max(work) >= finalAns:
        return
    for j in range(0, k):
        # optimization
        # we are aceesing half of tree only left part
        # no need to call right part of Tree
        if (j > 0) and (work[j] == work[j-1]):
            continue
        # action
        # if ith job include in jth worker
        work[j] += jobs[i]
        # recursive call
        Solve(i+1, k, n, jobs, work, ans)
        # backtracking
        work[j] -= jobs[i]


def minimumTimeRequired(jobs, k):
    jobs.sort(reverse=True)
    n = len(jobs)
    if n == k:
        return jobs[0]
    work = [0] * k
    assignmentsAns = 0
    index = 0
    Solve(index, k, n, jobs, work, assignmentsAns)
    return finalAns


jobs = [1, 2, 4, 7, 8]
k = 2
print(minimumTimeRequired(jobs, k))
# op - 11
