'''
301. Remove Invalid Parentheses
Given a string s that contains parentheses and letters,
remove the minimum number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals.
You may return the answer in any order.

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
Example 3:

Input: s = ")("
Output: [""]

- SOLN
- other question
- 20: Valid Parentheses - stack
- 1963: min number of swaps to make string valid
- 921: Minimum Add to Make Parentheses Valid

soln:
- you can find valid
  - no open is equal to close
  - 1st open than close
  - how many removal required to make its valid - stack
    - open stack push
      close - top open, than pop
            - pushed close brackets
      at last stack size == number of removal

'''


def getRemovalCount(s):
    # import pdb
    # pdb.set_trace()
    st = []
    for i in range(len(s)):
        ch = s[i]
        if ch == '(':
            st.append(ch)
        elif ch == ')':
            # check non empty stack
            if st and st[-1] == '(':
                st.pop()
            else:
                st.append(ch)
    return len(st)


def Solve(s, removalCnt, ans, map):
    # map if any itring creaeed mark its done or not
    # base case
    if map.get(s):
        return
    else:
        map[s] = True
    if removalCnt == 0:
        # nothing to remove
        # chck valid or not no gurantee for ans
        numRemoval = getRemovalCount(list(s))
        if numRemoval == 0:
            ans.append(s)
        return
    # which index bracket to remove - sabko remove karna haii
    for i in range(len(s)):
        # remove i
        # [) - slice operation
        leftStr = s[0:i]
        rightStr = s[i+1:]
        temp = leftStr + rightStr
        Solve(temp, removalCnt-1, ans, map)


def removeInvalidParentheses():
    s = "()())()"
    # print(getRemovalCount(list(s)))
    removeCnt = getRemovalCount(list(s))
    ans = []
    map = {}
    Solve(s, removeCnt, ans, map)
    print(ans)
    return ans


removeInvalidParentheses()
# op - ['(())()', '()()()']
