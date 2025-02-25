'''
refer: https://leetcode.com/problems/word-ladder-ii/
solutions/2367587/python-bfs-dfs-with-explanation-why-optimization-is-needed-to-not-tle/
126. Word Ladder II
A transformation sequence from word beginWord to word endWord using a
dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the
shortest transformation sequences from beginWord to endWord, or an empty list if
no such sequence exists. Each sequence should be returned as a list of the words
[beginWord, s1, s2, ..., sk].

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no
valid transformation sequence.

Soln:
source - differnt --> diff let letter = 1, than word 26 and check
in dictionary
already visited track

1.function - given two string than diff of them, differnt char count

TLE - Leetcode


'''
size = float('inf')


def isConvertible(a, b):
    # check diff is 1 or not
    # converting a to b
    # length diff cannot convertible
    if len(a) != len(b) or len(a) == 0:
        return False
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    if cnt == 1:
        return True
    return False


def Solve(src, dest, visited, wordList, res, path):
    # base case
    # if path end string match with destination
    global size
    if dest == path[-1]:
        # copy is required
        res.append(path[:])
        size = min(size, len(path))
        return
    # check each dictionary
    for word in wordList:
        # compare src with all dictionary words
        if isConvertible(src, word):
            if visited.get(word, False) is False:
                # than process it
                # include in path
                path.append(word)
                visited[word] = True
                # recursive call
                Solve(word, dest, visited, wordList, res, path)
                # undo the action
                path.pop()
                visited[word] = False


def findLadders(beginWord, endWord, wordList):
    result = []
    path = []
    visited = {}
    # path always sart from begin word
    path.append(beginWord)
    visited[beginWord] = True
    Solve(beginWord, endWord, visited, wordList, result, path)
    # print(result)
    finalAns = []
    for res in result:
        if len(res) == size:
            finalAns.append(res)
    print(finalAns)


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
findLadders(beginWord, endWord, wordList)
# op- [['hit', 'hot', 'dot', 'dog', 'cog'],
# ['hit', 'hot', 'lot', 'log', 'cog']]
