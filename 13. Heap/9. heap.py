'''
767. Reorganize String

Given a string s, rearrange the characters of s so that any two adjacent
characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""

SOLN:
PATTERN: Min cost to cut rope(solve using heap) same pattern is used
create map - char
jiski freq jyda haii usko jaldi consume kar lo ans string
max_heap: freq ke basis pe
strting 2 char nika lo from heap which is differnt in nature adjacent different

Pattern:
insert elements in heap you have make particular ordering
that i can get max 2 or 3 elements like that
pop that elements and do some operations and push again
jatbtk heap empty na ho jaye


'''


import heapq
from collections import defaultdict


def reorganizeString(s):
    # create mapping
    ans = []
    freq = defaultdict(lambda: 0)
    for i in range(len(s)):
        ch = s[i]
        freq[ch] = freq[ch] + 1
    # create max heaps
    maxHeap = []
    for key, value in freq.items():
        maxHeap.append((-value, key))
    heapq.heapify(maxHeap)
    # len(maxHeap) > 1 why because it have always two elements
    while len(maxHeap) > 1:
        first = heapq.heappop(maxHeap)
        second = heapq.heappop(maxHeap)
        ans.append(first[1])
        ans.append(second[1])
        first_count = -first[0]
        second_count = - second[0]
        first_count -= 1
        second_count -= 1
        if first_count != 0:
            heapq.heappush(maxHeap, (-first_count, first[1]))
        if second_count != 0:
            heapq.heappush(maxHeap, (-second_count, second[1]))
    # if any entries present in heaps
    if len(maxHeap) == 1:
        temp = heapq.heappop(maxHeap)
        temp_frq = -temp[0]
        if temp_frq == 1:
            ans.append(temp[1])
        else:
            # more than one string
            return ""
    return ''.join(ans)


s = "aab"
print(reorganizeString(s))
# aba
