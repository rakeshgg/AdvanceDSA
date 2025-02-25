'''
BackTrack - ISSUE !.e TLE
shortest - BFS, DFS, Disktra, HEAP, SET

SOLN = Backtracking + BFS
HOW TO APPLY BFS - LAYER by layer
DFS - depth - queue

Create Graph - using BFS - Adjancy List
Already used String - Visited - map/set()

- set create
- graph create
- similar to Tree level order Traversal

wrong please check once

'''

from queue import Queue


def findNextString(word, set_n):
    '''
    finding next string
    '''
    ans = []
    given_word = word
    word = list(word)
    for i in range(len(word)):
        currChar = word[i]
        # store all chr in range a - z
        for ch in range(ord('a'), ord('z')+1):
            # converting ancii to character
            word[i] = chr(ch)
            # old char is same as new char
            # new string should be present in dictionary
            if (chr(ch) == currChar) or (given_word in set_n):
                continue
            # push string in ans
            ans.append(''.join(word))
        word[i] = currChar
    return ans


def bfs(src, dest, set_n, adjList):
    # how to create a graph
    # layer by layer add/level order Traversal
    q = Queue()
    q.put(src)
    # if node is present in set than erase it
    if (src in set_n) != (dest in set_n):
        if src in set_n:
            set_n.remove(dest)
    inserted = {}
    inserted[src] = 1
    while not q.empty():
        visited = set()
        # particular layer processes
        for i in range(q.qsize(), 0, -1):
            # removing elements from queue
            currWord = q.get()
            neigh = findNextString(currWord, set_n)
            # adjancy list need to fill
            for nw in neigh:
                if not adjList.get(nw):
                    adjList[nw] = []
                adjList[nw].append(currWord)
                visited.add(nw)
                if not inserted.get(nw):
                    # queue not pushed
                    q.put(nw)
                    inserted[nw] = 1
        # remove string from previous layer
        for vis in visited:
            if vis in set_n:
                # remove
                set_n.remove(vis)


def Solve(src, dest, adjList, path, output):
    # base case
    if src == dest:
        output.append(path[:])
        return
    # if any node
    size = len(adjList[src])
    print(size)
    for i in range(size):
        path.append(adjList[src][i])
        Solve(adjList[src][i], dest, adjList, path, output)
        # undeo
        path.pop()


def findLadders(beginWord, endWord, wordList):
    adjList = {}
    path = []
    output = []
    set_n = set(wordList)
    # graph creation
    bfs(beginWord, endWord, set_n, adjList)
    print(adjList)
    # include src in path
    path.append(beginWord)
    # call backtrack solve function
    Solve(endWord, beginWord, adjList, path, output)
    return output


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(findLadders(beginWord, endWord, wordList))
