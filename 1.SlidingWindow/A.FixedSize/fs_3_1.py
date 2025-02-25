'''
Permutation in a String - 2nd methods


'''


def find_permutaion(str, pattern):
    char_freq_map = {}
    # compute the char_freq_map
    for char in pattern:
        if char not in char_freq_map:
            char_freq_map[char] = 0
        char_freq_map[char] += 1
    i, j = 0, 0
    matched = 0
    k = len(pattern)  # window size - size of pattern
    while j < len(str):
        # do calculation for j
        if str[j] in char_freq_map:
            char_freq_map[str[j]] -= 1
            if char_freq_map[str[j]] == 0:
                matched += 1
        window_size = j - i + 1
        if window_size < k:
            j += 1
        elif window_size == k:
            # possible ans to be find from calculation
            if matched == len(char_freq_map):
                # ans found
                return True
            # slide window
            # remove calculation for i
            if str[i] in char_freq_map:
                if char_freq_map[str[i]] == 0:
                    matched -= 1
                # print(matched)
                char_freq_map[str[i]] += 1
            i += 1
            j += 1
    return False


print(find_permutaion("oidbcaf", "abc"))
print(find_permutaion("odicf", "dc"))
print(find_permutaion("bcdxabcdy", "bcdyabcdx"))
print(find_permutaion("aaacb", "abc"))
