'''
1824. Minimum Sideway Jumps

There is a 3 lane road of length n that consists of n + 1 points
labeled from 0 to n. A frog starts at point 0 in the second
lane and wants to jump to point n. However, there could be obstacles along the way.

You are given an array obstacles of length n + 1 where each
obstacles[i] (ranging from 0 to 3) describes an obstacle on
the lane obstacles[i] at point i. If obstacles[i] == 0,
there are no obstacles at point i. There will be at most
one obstacle in the 3 lanes at each point.

For example, if obstacles[2] == 1, then there is an obstacle on lane 1 at point 2.
The frog can only travel from point i to point i + 1 on the same lane if
there is not an obstacle on the lane at point i + 1. To avoid obstacles,
the frog can also perform a side jump to jump to another lane (even if they are not adjacent)
at the same point if there is no obstacle on the new lane.

For example, the frog can jump from lane 3 at point 3 to lane 1 at point 3.
Return the minimum number of side jumps the frog needs to reach any lane at
point n starting from lane 2 at point 0.

Note: There will be no obstacles on points 0 and n.

Input: obstacles = [0,1,2,3,0]
Output: 2
Explanation: The optimal solution is shown by the arrows above. There are 2 side jumps (red arrows).
Note that the frog can jump over obstacles only when making side jumps (as shown at point 2).

Input: obstacles = [0,1,1,3,3,0]
Output: 0
Explanation: There are no obstacles on lane 2. No side jumps are required.

Input: obstacles = [0,2,1,0,3,0]
Output: 2
Explanation: The optimal solution is shown by the arrows above. There are 2 side jumps.

SOLN:
FROG --> END POSITION
frog start from 0th of lane2

frog Movements --> go strait if no obstacles
               --> got left
               --> got to Right

side priority high no jumps

# if current position equal to end position
if pos == n-1
   return 0
# straignt move if no obstacle
obs[0] = i -> 0th position pe obstacle ith lane pe haii
jis lane me maii khada hu uss lane me agali position me obstacle nahi hona chaiie
if obs[pos+1] != currlane

# side movements
lane1 - left movements
lan2 - straight movements
lan3 - right movements
for lane -> 1 to 3
    jaha khada haii wahi jump kare lane == currentlane not required
    jis lane me khada hu usko process nahi kar na haii no jump required
    to smae position again
    lane != currentLane and obs[pos]!=lane
    jump

'''


def solve(obs, currentlane, currpos):
    lastpos = len(obs) - 1
    # base case
    if currpos == lastpos:
        # no need to jump so zero
        return 0
    # straight movements
    if obs[currpos+1] != currentlane:
        # lane same rahega
        return solve(obs, currentlane, currpos+1)
    else:
        # side base movements
        ans = float('inf')
        for i in range(1, 4):
            if (i != currentlane) and (obs[currpos] != i):
                # side jumps, ek case solve karenge baki recusion
                ans = min(ans, 1 + solve(obs, i, currpos))
    return ans


# memeoijation
# currentlane, currpos change so 2D dp
# currentlane -> 0(imaginary), 1, 2, 3
# currpos -> 0 to n
def solveMem(obs, currentlane, currpos, dp):
    lastpos = len(obs) - 1
    # base case
    if currpos == lastpos:
        # no need to jump so zero
        return 0
    if dp[currentlane][currpos] != -1:
        return dp[currentlane][currpos]
    # straight movements
    finalAns = 0
    if obs[currpos+1] != currentlane:
        # lane same rahega
        finalAns = solveMem(obs, currentlane, currpos+1, dp)
    else:
        # side base movements
        ans = float('inf')
        for i in range(1, 4):
            if (i != currentlane) and (obs[currpos] != i):
                # side jumps, ek case solve karenge baki recusion
                ans = min(ans, 1 + solveMem(obs, i, currpos, dp))
        finalAns = ans
    dp[currentlane][currpos] = finalAns
    return dp[currentlane][currpos]


# Bottom Up
#
def solveTab(obs):
    # bottom up frog destination se source pe jata haii
    # ans = min(ans, dp[i][currpos+1])
    # why currpos+1
    # i -> current lane se dusari lane me jane wala ho top down
    # iss current lane me i se kayse pauche hoge - bottom up
    # currpos +1 next position
    '''
    check your self
    # required min ans so initialize with intmax
    n = len(obs)
    dp = [[float('inf')]*(n+1) for _ in range(4)]
    # base case analysis
    # last index col me put zero
    for i in range(0, 4):
        dp[i][n-1] = 0
    # find range
    # lane 2 to any range not clear
    # [2, 0] ->[1, n], [2, n], [3, n]
    # bottom up [1, n], [2, n], [3, n] -> [2, 0]
    # lane -> 1, 2, 3
    # pos -> 0 to n so here n to 0
    for currentlane in range(1, 4):
        for currpos in range(n-2, -1, -1):
            finalAns = 0
            if obs[currpos+1] != currentlane:
                # lane same rahega
                finalAns = dp[currentlane][currpos+1]
            else:
                # side base movements
                ans = float('inf')
                for i in range(1, 4):
                    if (i != currentlane) and (obs[currpos] != i):
                        # side jumps, ek case solve karenge baki recusion
                        ans = min(ans, 1 + dp[i][currpos])
                finalAns = ans
            dp[currentlane][currpos] = finalAns
    return min(dp[2][0], min(1 + dp[1][0], 1 + dp[3][0]))
    '''


def minSideJumps(obstacles):
    # currentlane = 2
    # currpos = 0
    # return solve(obstacles, currentlane, currpos)
    # n = len(obstacles)
    # dp = [[-1]*(5) for _ in range(n)]
    # return solveMem(obstacles, currentlane, currpos, dp)
    return solveTab(obstacles)


obstacles = [0, 2, 1, 0, 3, 0]
print(minSideJumps(obstacles))
# 2
