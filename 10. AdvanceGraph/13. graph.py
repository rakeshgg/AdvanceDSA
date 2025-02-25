'''
207. Course Schedule

There are a total of numCourses courses you have to take,
labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [ai, bi] indicates
that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course
0 you have to first take course 1.
Return true if you can finish all courses.
Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take
course 0 you should also have finished course 1. So it is impossible.

I thing depend on other -> so toplogical sort
its edge list -> but in reverse order

lets create adjancy list

'''

from collections import defaultdict
from collections import deque


def topoSortBFSCycle(n, adjList):
    ans = []
    q = deque()
    indegree = {}
    for i in range(n):
        indegree[i] = 0
    for i in adjList.items():
        _, nbrs = i[0], i[1]
        for nbr in nbrs:
            indegree[nbr] += 1
    for i in range(n):
        if indegree.get(i) == 0:
            q.append(i)
    while len(q):
        fNode = q.pop()
        ans.append(fNode)
        for nbr in adjList[fNode]:
            indegree[nbr] -= 1
            if indegree[nbr] == 0:
                q.append(nbr)
    # cycle detection
    if len(ans) == n:
        # valid topo sort
        return True
    else:
        # cycle case
        return False


def canFinish(numCourses, prerequisites):
    # creation of adjnacy list
    adjList = defaultdict(lambda: [])
    for task in prerequisites:
        u = task[0]
        v = task[1]
        # edge is from v to u
        adjList[v].append(u)
    # cycle case me canFinish karna impossible
    # cycle and dependecy
    ans = topoSortBFSCycle(numCourses, adjList)
    print(ans)


numCourses = 2
prerequisites = [[1, 0]]
canFinish(numCourses, prerequisites)
