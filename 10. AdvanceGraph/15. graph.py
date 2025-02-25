'''
127. Word Ladder

A transformation sequence from word beginWord to word endWord using a
dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of
words in the shortest transformation sequence from beginWord to endWord, or 0 if no such
sequence exists.

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is
"hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is
no valid transformation sequence.

observation:
from word beginWord to word endWord using a -> Edit ditance like thought
beginWord = "hit", endWord = "cog",  wordList = ["hot","dot","dog","lot","log","cog"]

hit -> cog
in tranformaion 1 char diff all other are same
shortest path -> traversal every edge weight to 1

1 char change -> h -> (a to z) -> 25 option
shortest path -> option
BFS -> dy-deafult shortest path gives


'''


from collections import deque


def ladderLength(beginWord, endWord, wordList):
    q = deque()
    # word and count
    q.append((beginWord, 1))
    # copy of word list
    st = set(wordList)
    # in place of set you can use dict also
    # jo vi word queue me insert karunga usko set se remove kar dunga
    # set remove will return exception if not found in set
    # discard is similar but no exceptions
    st.discard(beginWord)
    while len(q):
        fNode = q.pop()
        currString, currCount = fNode
        # check if you are not reach to detination
        if currString == endWord:
            return currCount
        # char replacemnts
        # making string as mutable
        currString = list(currString)
        for index in range(len(currString)):
            originalChar = currString[index]
            # hr index pe jo value haii usko a to z se replace karna haii
            for ch in range(ord('a'), ord('z')+1):
                currString[index] = chr(ch)
                # check if new string present in sets or not
                # if present in set insert in queue
                new_string = ''.join(currString)
                if new_string in st:
                    q.append((new_string, currCount+1))
                    st.remove(new_string)
            # once inserted make char in original positions
            # bring back char in its original state
            currString[index] = originalChar
    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(ladderLength(beginWord, endWord, wordList))
