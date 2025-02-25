'''
Find Middle Elements in Stack - rest data remain same
Pattern:
-> Recursion is Stack
-> during recursive call - pop elemnts store in temp at every state
- during return - once ans Find -> push elemenst in stack

Pattern - Important
- You have 1 state of stack you want to perform some operation inside it
- Do Recursive Calls
- Jab wapas aeoge return me jo operation kie the unko reverse karna haii

'''


def printMiddleEle(s, totalSize):
    if len(s) == 0:
        print("There is no elements in stack")
        return
    # base case
    if len(s) == (totalSize//2 + 1):
        # print top elemnts
        print(f'middle elemnts is {s[-1]}')
        return
    temp = s.pop()
    print(temp)
    # recursive call
    printMiddleEle(s, totalSize)
    # backTrack
    s.append(temp)
    print(s)


stack = []
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
stack.append(60)
stack.append(70)
printMiddleEle(stack, len(stack))
print(stack)
