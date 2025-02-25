class Solution:
    def frequencySort(self, s):
        # your code goes here
        # [abababcdefcccc]
        from collections import Counter
        # freq count map
        freq = Counter(s)
        # highest fre first if equal use character
        sorted_chars = sorted(freq.keys(), key=lambda ch: (-freq[ch], ch))
        # freq.sort(key=lambda x: (-x[0], x[1]))
        # sorted(iterable, key=None, reverse=False)
        # list.sort(key=None, reverse=False)
        return sorted_chars


from collections import Counter
iterable = []
counter_obj = Counter(iterable)


# Time and space computaion in Recursion
# let function execution time is -- O(1)
# find number of time function call -- let say n times 
# TC - O(N)

# space complexity
# size of stack at a particular time
# stack space + inside recsuion any space 
