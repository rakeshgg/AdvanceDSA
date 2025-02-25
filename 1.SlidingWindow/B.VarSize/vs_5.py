'''
Longest Substring with Same Letters after Replacement

Given a string with lowercase letters only
if you are allowed to replace no more than k letters with any letter
find the length of the longest substring having the same letters after
replacement.

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest
repeating substring "bbbbb".

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring
"bbbb".

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest
repeating substring "ccc".

WS - MAX FREQ CHAR in window(HOW to check) - condition
condition <= k , window is valid
MAX FREQ CHAR in window(HOW to check) - O(26)

WS - MaxFrq in MAP during increasing window
WS - MaxFrq > k, MaxFrq not required as minmzing window and condition
distinct elemnts other than max freq - (j - i + 1) - max_freq
'''


def character_replacement(string, k):
    max_freq = float('-inf')
    char_map = {}
    res = 0
    i, j = 0, 0
    while j < len(string):
        # do calculation for j
        if string[j] not in char_map:
            char_map[string[j]] = 0
        char_map[string[j]] += 1
        max_freq = max(max_freq, char_map[string[j]])
        if (j - i + 1) - max_freq <= k:
            # valid ws
            res = max(res, j-i+1)
            j += 1
        elif (j - i + 1) - max_freq > k:
            # invalid ws
            while (j - i + 1) - max_freq > k:
                char_map[string[i]] -= 1
                # not required to calulctate frq as minimizing ws
                i += 1
            j += 1
    return res


print(character_replacement("aabccbb", 2))
print(character_replacement("abbcb", 1))
print(character_replacement("abccde", 1))
