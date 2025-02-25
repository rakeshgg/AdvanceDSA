'''

Permutation in a String
Given a string and a pattern, find out if the string contains any permutation
of the pattern.

Permutation is defined as the re-arranging of the characters of the string,
for example, “abc”
has the following six permutations:
abc
acb
bac
bca
cab
cba
If a string has 'n' distinct characters it will have
n! permutations.


Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation
of the given pattern.

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string
as a substring.

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given
pattern.

Fixed size window problem - ws given len of pattern

'''


def find_permutaion(str, pattern):
    char_freq_map = {}
    # compute the char_freq_map
    for char in pattern:
        if char not in char_freq_map:
            char_freq_map[char] = 0
        char_freq_map[char] += 1
    i, j = 0, 0
    matched = len(char_freq_map)
    k = len(pattern)  # window size - size of pattern
    while j < len(str):
        # do calculation for j
        if str[j] in char_freq_map:
            char_freq_map[str[j]] -= 1
            if char_freq_map[str[j]] == 0:
                matched -= 1
        window_size = j - i + 1
        if window_size < k:
            j += 1
        elif window_size == k:
            # possible ans to be find from calculation
            if matched == 0:
                # ans found
                return True
            # sliding window
            # remove calculation for i
            if str[i] in char_freq_map:
                if char_freq_map[str[i]] == 0:
                    matched += 1
                char_freq_map[str[i]] += 1
            i += 1
            j += 1
    return False


print(find_permutaion("oidbcaf", "abc"))
print(find_permutaion("odicf", "dc"))
print(find_permutaion("bcdxabcdy", "bcdyabcdx"))
print(find_permutaion("aaacb", "abc"))
