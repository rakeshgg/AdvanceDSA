'''
Insert Top elemnts in Bottom of stack
same as Prev Pattern:
base case -> bottom insert -> stack empty than insert target
waps -> pop elemnts ko push kar do

'''


def solve(s, target):
    # base case
    if len(s) == 0:
        s.append(target)
        return
    topElement = s.pop()
    print(topElement)
    # rec call
    solve(s, target)
    # backtrack
    s.append(topElement)
    print(s)


def inserAtBottom(s):
    if len(stack) == 0:
        print("stack is empty cannot insert at bottom")
        return
    target = s.pop()
    solve(s, target)


stack = []
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
print(stack)
inserAtBottom(stack)
print(stack)
