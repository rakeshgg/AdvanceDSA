'''
2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

A critical point in a linked list is defined as either a local maxima or a local minima.

A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

Given a linked list head, return an array of length 2 containing [minDistance, maxDistance]
where minDistance is the minimum distance between any two distinct critical points and
maxDistance is the maximum distance between any two distinct critical points.
If there are fewer than two critical points, return [-1, -1].

Input: head = [3,1]
Output: [-1,-1]
Explanation: There are no critical points in [3,1].

Input: head = [1,3,2,2,3,2,2,2,7]
Output: [3,3]
Explanation: There are two critical points:
- [1,3,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
- [1,3,2,2,3,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
Both the minimum and maximum distances are between the second and the fifth node.
Thus, minDistance and maxDistance is 5 - 2 = 3.
Note that the last node is not considered a local maxima because it does not have a next node.

'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def nodesBetweenCriticalPoints(head):
    # minDist, maxDist
    ans = [-1, -1]
    # atleast 3 node shoudl be there
    prev = head
    if prev is None:
        return ans
    curr = head.next
    if curr is None:
        return ans
    nxt = head.next.next
    if not nxt:
        return ans
    # find min and max
    # max - 1st critical and last critcal diff
    # min - two distict min - node you are standing - last cp distance
    firstCP = -1
    lastCP = -1
    minDist = float('inf')
    i = 1
    while nxt:
        # cp either local maxima or minima
        isCP = ((curr.val > prev.val) and (curr.val > nxt.val)) or ((curr.val < prev.val) and (curr.val < nxt.val))
        if isCP and firstCP == -1:
            firstCP = i
            lastCP = i
        elif isCP:
            minDist = min(minDist, i-lastCP)
            lastCP = i
        i += 1
        prev = prev.next
        curr = curr.next
        nxt = nxt.next
    if lastCP == firstCP:
        # only one cp was found
        return ans
    else:
        ans[0] = minDist
        ans[1] = lastCP - firstCP
        return ans
