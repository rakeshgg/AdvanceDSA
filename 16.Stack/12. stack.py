'''
Largest Area in Histogram

- Next Smaller Elements
  check in right side
  [2, 1, 4, 3]
   1 -1  3  -1   -> next smaller elemnts

Approch - BruteForce - 2 Loops
                       check windows
        for(i=0, <n)
          for (i+1, <n)
    O(n^2)
Approch2:
    Going through Left to right -> O(n^2)
    Going Right Through Left -> ? which DS
        -> last Elemnts ans = -1
        Taking Stack
        push -1
        get xota from stack if not found pop till xota found
        else push xota in stack
    A. stack push -1
    B. array k me R to L jaeo aur check stack me koi xota elements exit karta haii ki nahi
       pop() karte raho mill gya store kar lo
    c. Jis elements pe khade ho usko push kar do

Previous Smaller Elemnets
[2, 1, 4, 3]
 -1, -1, 1, 1
-> Left to right direction

TC: every elemnt is checking once in stack
    worst case me n elemnts push and pop -> n + n = O(n)

-- 2 for loops in this bruteforce approch - o(n^2)

'''


def getNextSmallerEle(v):
    ans = [-1] * len(v)
    st = [-1]
    # from right to Left Loop
    for i in range(len(v)-1, -1, -1):
        curr = v[i]
        # pop till lesser elements found in stack
        while st[-1] >= curr:
            st.pop()
        # chotta elemnt mil chuka haii ans store
        ans[i] = st[-1]
        # push kar do current elements ko
        st.append(curr)
    return ans


def getPrevSmallerEle(v):
    ans = [-1] * len(v)
    st = [-1]
    # from Left to Right Loop
    for i in range(0, len(v)):
        curr = v[i]
        # pop till lesser elements found in stack
        while st[-1] >= curr:
            st.pop()
        # chotta element mil chuka haii ans store
        ans[i] = st[-1]
        # push kar do current elements ko
        st.append(curr)
    return ans


if __name__ == '__main__':
    v = [2, 1, 4, 3]
    print(getNextSmallerEle(v))
    print(getPrevSmallerEle(v))

# [1, -1, 3, -1]
# [-1, -1, 1, 1]