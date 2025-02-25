'''
There are n people standing in the queue. They are numbered from 0 to n-1 in left to right order.
You are given with an array heights of distinct integers where heights[i] is the height of
the ith person.

A person can see another person to their right if everybody in between is shorter than both of them.

Return an array answer of length n where answer[i] is the number of people the ith person can see
to their right in the queue.

SOLUTION
The questions seems to be tailor made for our templates here. Intuition
- for every person we decide only to things.

The next person with greater or equal height (no person after this
would be visible to the current person). But multiple people behind
the current person with bigger height can see the current person.
Let's take care of them in the second point.

The previous person with strictly greater height than the current person.
1 and 2 both select mutually exclusive people. Every time we find a person
from both the cases, we increase their corresponding number of visisble people by 1.

We should be able to use the merged template for next greater
and previous greater for this question.

'''


def canSeePersonsCount(heights):
    stack = []
    answer = [0] * len(heights)

    for i in range(len(heights)):
        while stack and heights[stack[-1]] <= heights[i]:
            # Next greater section
            stackTop = stack.pop()
            # Process
            answer[stackTop] += 1

        if stack:
            # Previous greater section
            # Process
            answer[stack[-1]] += 1

        stack.append(i)

    return answer


print(canSeePersonsCount([10, 6, 8, 5, 11, 9]))
# [3, 1, 2, 1, 1, 0]
print(canSeePersonsCount([5, 1, 2, 3, 10]))
# [4, 1, 1, 1, 0]
