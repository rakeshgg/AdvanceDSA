'''
First none Repeating char in Stream
https://www.geeksforgeeks.org/find-first-non-repeating-character-stream-characters/
Given a stream of characters, find the first non-repeating character from the stream. You need to tell
the first non-repeating character in O(1) time at any moment.

Soln -> left to right check and see first not repeated
-> har char -> count store -> map

- char -> fre incremnts
- include char in queue : potential char to become none repating

'''


from collections import deque
from collections import defaultdict


def FirstNonRepeating(input_stream):
    ans = []
    map = defaultdict(lambda: 0)
    q = deque()
    for char in input_stream:
        # incremnt frquncy
        map[char] += 1
        # push into queue
        q.append(char)
    # check in front of queue repating char
    while len(q):
        # pop from left
        front = q.popleft()
        if map[front] == 1:
            ans.append(front)
    # if queue is empty
    if not len(q):
        ans.append("#")
    return ''.join(ans)


A = "aabc"
ans = FirstNonRepeating(A)
print(ans)
