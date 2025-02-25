'''
Distribute Repeating Integers

You are given an array of n integers, nums,
where there are at most 50 unique values in the array.
You are also given an array of m customer order quantities,
quantity, where quantity[i] is the amount of integers the
ith customer ordered. Determine if it is possible to distribute nums such that:

The ith customer gets exactly quantity[i] integers,
The integers the ith customer gets are all equal, and
Every customer is satisfied.
Return true if it is possible to distribute nums according to the above conditions.

Example 1:

Input: nums = [1,2,3,4], quantity = [2]
Output: false
Explanation: The 0th customer cannot be given two different integers.
Example 2:

Input: nums = [1,2,3,3], quantity = [2]
Output: true
Explanation: The 0th customer is given [3,3]. The integers [1,2] are not used.
Example 3:

Input: nums = [1,1,2,2], quantity = [2,2]
Output: true
Explanation: The 0th customer is given [1,1], and the 1st customer is given [2,2].

soln
0th customer 2 inegers required - 3, 3

how know false:
count frquency of elements
qunatity satify than priority to big numbers
- Sort Qunatity array in desecending order - biggest qunatity process first

- action : integer required

- Optimization can be done using DP/Bit masking


'''


def Solve(quantity, count, index):
    # base case
    if index == len(quantity):
        return True
    # 1 case solve
    for key, freq in count.items():
        if freq >= quantity[index]:
            # update count as freq is ued fro index 0
            # action
            count[key] = count[key] - quantity[index]
            # Recusrion
            aageKaSol = Solve(quantity, count, index+1)
            if aageKaSol:
                return True
            # backTrack action undeo
            count[key] = count[key] + quantity[index]
    return False


def canDistribute(nums, quantity):
    count = {}
    # count frquncy of nums array
    for i in range(len(nums)):
        if not count.get(nums[i]):
            count[nums[i]] = 0
        count[nums[i]] += 1
    # sort Qunatity
    quantity.sort(reverse=True)
    # index which need to process
    ans = Solve(quantity, count, 0)
    return ans


nums = [1, 1, 2, 2]
quantity = [2, 2]
print(canDistribute(nums, quantity))
