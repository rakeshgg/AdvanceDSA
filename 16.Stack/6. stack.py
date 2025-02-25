'''
Reverse a stack
- Ek case Hum solve karenge Baki recursion karega

'''


def insertAtBottom(s, target):
    # base case
    if len(s) == 0:
        s.append(target)
        return
    topElement = s.pop()
    # rec call
    insertAtBottom(s, target)
    # backtrack
    s.append(topElement)


def reverseStack(s):
    # base case
    # stack hi empty ho gya
    if len(s) == 0:
        return
    target = s.pop()
    # target insert at bottom jab stack reverse ho jata haii
    print(target)
    reverseStack(s)
    # insert at bottom target ko
    insertAtBottom(s, target)


stack = []
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
print(stack)
reverseStack(stack)
print(stack)
