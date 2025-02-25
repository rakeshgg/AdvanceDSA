'''
https://leetcode.com/problems/car-fleet-ii/
1776. Car Fleet II

Example 1:

Input: cars = [[1,2],[2,1],[4,3],[7,2]]
Output: [1.00000,-1.00000,3.00000,-1.00000]
Explanation: After exactly one second, the first car will
collide with the second car, and form a car fleet with
speed 1 m/s. After exactly 3 seconds, the third car will
collide with the fourth car, and form a car fleet with speed 2 m/s.

Approch:
collide jab age wali gai slow chal raha ho than collide
har point pe -> is there any car ahed of me which we can collide start from right to left
collision time = (9-6)/(3-1) = 1.5

Better Soln: Maintain stack
 - Top Stack

'''


def getCollisionTimes(cars):
    # collision time of ith cars with next cars is ans
    pass
