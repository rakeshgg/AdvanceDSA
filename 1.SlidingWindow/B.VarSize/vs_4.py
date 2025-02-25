'''
Given a string, find the length of the longest substring which has no
repeating characters.

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters
are "abc" & "cde".

previous problem - Longest Substring with K Distinct Characters
in This problem - Longest Substring with ALL Distinct Characters
                - j - i + 1 - all should be distict
K - Not Given - ALL unique Character given
   condition become -  #len(map) == j-i+1
   previously k is constants and k char unique in WS
'''


def length_of_longest_substring_distinct_char(string):
    max_len = float('-inf')
    char_map = {}
    i, j = 0, 0
    while j < len(string):
        # do calculation store each char in map with its count
        if string[j] not in char_map:
            char_map[string[j]] = 0
        char_map[string[j]] += 1
        # do till condition meet
        # if never run
        # if len(char_map) > j-i+1:
        #    j += 1
        if len(char_map) == j-i+1:
            # calculate ans from calculation
            max_len = max(max_len, j-i+1)
            j += 1
        elif len(char_map) < j-i+1:
            # remove calculation for i
            # there should be a duplicate
            # removing duplicate
            while (len(char_map) < j-i+1):
                char_map[string[i]] -= 1
                if char_map[string[i]] == 0:
                    del char_map[string[i]]
                i += 1
            j += 1
    return max_len


print(length_of_longest_substring_distinct_char("aabccbb"))
print(length_of_longest_substring_distinct_char("abbbb"))
print(length_of_longest_substring_distinct_char("abccde"))
