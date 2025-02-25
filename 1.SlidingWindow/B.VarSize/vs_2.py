'''
Longest Substring with K Distinct Characters (medium)

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters
is "araa".

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than
'1' distinct characters is "aa".

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3'
distinct characters are
"cbbeb" & "bbebi".

'''
# to find longest substing with repeting char
# - dict is used to store and track it
# len(dict) - O(1),  if not then use one external variables to do it
# TC - O(N), SC:O(K+1)


def longest_string_with_k_ditinct(string, k):
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


print(longest_string_with_k_ditinct("araaci", 2))
print(longest_string_with_k_ditinct("araaci", 1))
print(longest_string_with_k_ditinct("cbbebi", 3))
