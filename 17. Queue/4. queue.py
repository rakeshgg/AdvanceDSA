'''
https://leetcode.com/problems/gas-station/

134. Gas Station
There are n gas stations along a circular route, where the amount of gas at the ith
station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
from the ith station to its next (i + 1)th station. You begin the journey with
an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index
if you can travel around the circuit once in the clockwise direction, otherwise
return -1. If there exists a solution, it is guaranteed to be unique

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

circular - which index to start circular route finsih
soln: p0,  p1,   p2,   p3,   p4
     g[0], g[1], g[2], g[3], g[4]

Let say -> 0th index start
 balance, dist
 - check at every index -> 2 loops -> TC:O(n^2)

 Approch2: ->Optimization
 old approch: already know fron 0th to 3rd not possible then why to chekc again from 1 to 3
 har log aage petrol ko 0 ya >0 petrol dega
 jha pe flow break ho raha haii waha se check karo again
 -> Think front and rear tearm
 -> movement possible -> rear++  -> petrol - distance > 0 movements possible
 -> movements not possible -> front = rear + 1, rear = front

TC - > O(n), SC-> O(1)

'''


def canCompleteCircuit(gas, cost):
    # kitna petorl kam padd gya
    deficit = 0
    # kitna paetorl bacha hua haii
    balance = 0
    # kha se start kar rahe ho
    start = 0
    for i in range(len(gas)):
        balance += gas[i] - cost[i]
        if balance < 0:
            # petrol ki kami
            # sabb deficit add karta haii
            deficit += balance
            # jha pe fail hua uske agle index se suru karo
            start = i + 1
            balance = 0
    if deficit + balance >= 0:
        return start
    else:
        return -1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(canCompleteCircuit(gas, cost))
# 3
