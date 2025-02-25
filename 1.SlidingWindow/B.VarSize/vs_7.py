'''
Smallest Window containing Substring
or
Minimum Window Substring

Given a string and a pattern, find the smallest substring in
the given string which has all the characters of the given pattern

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of
the pattern is "abdec"


Input: String="abdabca", Pattern="abc"
Output: "abc"
Explanation: The smallest substring having all characters
of the pattern is "abc"

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all
characters of the pattern.

pattern all letter in same qunatity should present in str
-ve count char in maps means these are used latter for us
these extra no of char added

previoulsy removing from map itself when its zero


'''


def find_min_window_substring_var_size(str, pattern):
    char_freq_map = {}
    # store freq map of pattern
    for char in pattern:
        if char not in char_freq_map:
            char_freq_map[char] = 0
        char_freq_map[char] += 1
    matched = len(char_freq_map)
    i, j = 0, 0
    min_len = float("inf")
    start = 0
    while j < len(str):
        if str[j] in char_freq_map:
            char_freq_map[str[j]] -= 1
            if char_freq_map[str[j]] == 0:
                matched -= 1
        # char_freq_map all are zero means all
        # req items are present in window, if -ve some extra are there
        # removing extra character in window - optimization of window size
        if matched == 0:
            # possible ans, remove extra character for this
            while matched == 0:
                if str[i] in char_freq_map:
                    char_freq_map[str[i]] += 1
                    if char_freq_map[str[i]] == 1:
                        matched += 1
                        # possible ans
                        if j - i + 1 < min_len:
                            min_len = j - i + 1
                            start = i
                i += 1
        j += 1
    if min_len > len(str):
        return ""
    return str[start: start + min_len]


print(find_min_window_substring_var_size('aabdec', 'abc'))
print(find_min_window_substring_var_size('abdabca', 'abc'))
print(find_min_window_substring_var_size('adcad', 'abc'))
