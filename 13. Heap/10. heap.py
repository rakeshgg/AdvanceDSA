'''
1405. Longest Happy String

A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string.
If there are multiple longest happy strings, return any of them. If there is no
such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.

Pattern Used: similar to previous


'''


import heapq


def longestDiverseString(a, b, c):
    maxHeap = []
    if a > 0:
        maxHeap.append((-a, 'a'))
    if b > 0:
        maxHeap.append((-b, 'b'))
    if c > 0:
        maxHeap.append((-c, 'c'))
    heapq.heapify(maxHeap)
    ans = []
    while len(maxHeap) > 1:
        first = heapq.heappop(maxHeap)
        second = heapq.heappop(maxHeap)
        first_count = -first[0]
        second_count = - second[0]
        if first_count >= 2:
            # added 2 times same char
            ans.append(first[1])
            ans.append(first[1])
            first_count -= 2
        else:
            # gurantee 1 count hoga
            ans.append(first[1])
            first_count -= 1
        # here people make mistake second_count >= first_count
        if second_count >= 2 and second_count >= first_count:
            # added 2 times same char
            ans.append(second[1])
            ans.append(second[1])
            second_count -= 2
        else:
            # gurantee 1 count hoga
            ans.append(second[1])
            second_count -= 1
        if first_count > 0:
            heapq.heappush(maxHeap, (-first_count, first[1]))
        if second_count > 0:
            heapq.heappush(maxHeap, (-second_count, second[1]))
    # come out of heap
    # what if elemnts left in heap
    if len(maxHeap) == 1:
        temp = heapq.heappop(maxHeap)
        temp_count = -temp[0]
        if temp_count >= 2:
            # added 2 times same char
            ans.append(temp[1])
            ans.append(temp[1])
            temp_count -= 2
        else:
            # gurantee 1 count hoga
            ans.append(temp[1])
            temp_count -= 1
    return ''.join(ans)


a = 7
b = 1
c = 0
print(longestDiverseString(a, b, c))
