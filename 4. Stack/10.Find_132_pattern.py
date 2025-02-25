'''
Given an array of n integers nums, a 132 pattern is a subsequence of
three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.


The question wants to find a triplet of three numbers from an array
such that their indices and numbers fulfill this condtion
- i < j < k and arr[i] < arr[k] < arr[j]
You can see that we are making a pattern like 1 - 3 - 2


Alternate way of asking the same question -

Find previous greater element for each number a.
Once the previous greater element x is found, check the previous minimum element for x
If the previous minimum number is smaller than the number a, we know the pattern exists

'''


def find132pattern(nums):
    minimums = [0] * len(nums)
    stack = []
    for i in range(len(nums)):
        # Set up minimums
        if i == 0:
            minimums[i] = 0
        else:
            if nums[i] < nums[minimums[i - 1]]:
                minimums[i] = i
            else:
                minimums[i] = minimums[i - 1]
        # Using a template for finding previous greater elements
        # Find the previous greater element and build a monotonic decreasing stack
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        # If there is a previous greater element, the stack will not be empty
        if stack:
            # If the previous minimum for the previous greater element is less than
            # the current number, then return True
            if nums[minimums[stack[-1]]] < nums[i]:
                return True
        stack.append(i)
    return False


print(find132pattern([3, 1, 4, 2]))
print(find132pattern([1, 2, 3, 4]))
