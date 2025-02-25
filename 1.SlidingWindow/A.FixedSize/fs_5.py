'''
Words Concatenation
Substring with Concatenation of All Words
Time Complexity : O(N - K) * K

Given a string and a list of words, find all the starting indices
of substrings in the given string that are a concatenation of all
the given words exactly once without any overlapping of words.
It is given that all words are of the same length

Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the
words are "catfox" & "foxcat"


Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox"

This problem follows the Sliding Window pattern and has a
lot of similarities with Maximum Sum Subarray of Size K.
We will keep track of all the words in a HashMap and try
to match them in the given string. Here are the set of steps for our algorithm:

'''


def findSubstring(str, list_words):
    ans = []
    if len(list_words) == 0 or len(list_words[0]) == 0:
        return ans
    # uniform across ths list
    size_word = len(list_words[0])
    # no of words in a list
    word_count = len(list_words)
    # total char in a list
    total_char_in_list = size_word * word_count
    if total_char_in_list > len(str):
        return ans
    # store map of words from list
    word_map_frq = {}
    for word in list_words:
        if word not in word_map_frq:
            word_map_frq[word] = 0
        word_map_frq[word] += 1
    for i in range(0, len(str) - total_char_in_list + 1):
        count = word_count
        j = i
        temp_hash_map = word_map_frq.copy()
        while j < i + total_char_in_list:
            next_word = str[j:j+size_word]
            # If word not found or if frequency of
            # current word is more than required simply break.
            if next_word not in word_map_frq or temp_hash_map[next_word] == 0:
                break
            else:
                # if next_word in word_map_frq
                temp_hash_map[next_word] -= 1
                count -= 1
            # increment for next words
            j += size_word
        # ans
        # when all the words in the list are in substring
        if count == 0:
            ans.append(i)
    return ans


print(findSubstring("barfoothefoobarman", ["foo", "bar"]))
print(findSubstring("catfoxcat", ["cat", "fox"]))
print(findSubstring("catcatfoxfox", ["cat", "fox"]))
