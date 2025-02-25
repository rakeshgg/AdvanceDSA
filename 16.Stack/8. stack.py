'''
Sort A Stack
- soln same as previous pattern Reversed one

'''


def insertSorted(s, target):
    # empty case
    if len(s) == 0:
        # single elements sorted
        s.append(target)
        return
    # base case
    if s[-1] >= target:
        s.append(target)
        return
    topElement = s.pop()
    insertSorted(s, target)
    # wapas aate hue
    s.append(topElement)


def sortStack(s):
    # base case stack empty
    if len(s) == 0:
        return
    topElement = s.pop()
    sortStack(s)
    insertSorted(s, topElement)


if __name__ == '__main__':
    stack = []
    stack.append(50)
    stack.append(40)
    stack.append(30)
    stack.append(20)
    stack.append(70)
    print(stack)
    sortStack(stack)
    print(stack)
