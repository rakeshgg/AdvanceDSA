'''
String Anagrams

Given a string and a pattern, find all anagrams of the pattern in the given
string.

Anagram is actually a Permutation of a string.
For example, “abc” has the following six anagrams:
abc
acb
bac
bca
cab
cba

Write a function to return a list of starting indices of
the anagrams of the pattern in the given string.

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq"
and "qp".

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in
the given string are "bca", "cab", and "abc".

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
    ans = []
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
                # return True
                ans.append(i)
            # slide window
            # remove calculation for i
            if str[i] in char_freq_map:
                if char_freq_map[str[i]] == 0:
                    matched += 1
                char_freq_map[str[i]] += 1
            i += 1
            j += 1
    return ans



print(find_permutaion("ppqpp", "pq"))
print(find_permutaion("abbcabc", "abc"))
