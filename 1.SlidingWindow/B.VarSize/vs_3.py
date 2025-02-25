'''
Given an array of characters where each character represents a fruit tree,
you are given two baskets and your goal is to put maximum number of fruits
in each basket. The only restriction is that each basket can have only one
type of fruit

You can start with any tree, but once you have started you can’t skip a tree.
You will pick one fruit from each tree until you cannot, i.e., you will stop
when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A'
in the other from the subarray ['C', 'A', 'C']

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

This problem transforms to
Longest Substring with at most 2 distinct characters - K=2

'''


def longest_string_with_2_ditinct(string, k):
    max_len = float('-inf')
    char_map = {}
    i, j = 0, 0
    while j < len(string):
        # do calculation store each char in map with its count
        if string[j] not in char_map:
            char_map[string[j]] = 0
        char_map[string[j]] += 1
        # do till condition meet
        if len(char_map) < k:
            j += 1
        elif len(char_map) == k:
            # calculate ans from calculation
            max_len = max(max_len, j-i+1)
            j += 1
        elif len(char_map) > k:
            # remove calculation for i
            while (len(char_map) > k):
                char_map[string[i]] -= 1
                if char_map[string[i]] == 0:
                    del char_map[string[i]]
                i += 1
            j += 1
    return max_len


print(longest_string_with_2_ditinct(['A', 'B', 'C', 'A', 'C'], 2))
print(longest_string_with_2_ditinct(['A', 'B', 'C', 'B', 'B', 'C'], 2))
