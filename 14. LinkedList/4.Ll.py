'''
Reverse Linked List
IP
[10] -> [20] -> [30] -> [40]
OP
[10] <- [20] <- [30] <- [40] <-

Harr node apne pixe wale node ko point kare
      [10] -> [20] -> [30] -> [40]
    NULL -> 10 ke prev NULL haii
    1. case solve: prev = None
                   curr = head
                   curr.next = prev

    prev, curr, next
    None,  a,   a.next

    Shift, prev, curr, next
    next is used to track other list save from lost

'''


class SLL:
    def __init__(self):
        self.head = None


def reverseSLL(prev, curr):
    # base case
    if curr is None:
        # LL is was reversed
        # prev is head pointer
        return prev
    # 1 case solve recursion will take care
    forward = curr.next
    curr.next = prev
    reverseSLL(curr, forward)


def reverseSLLLoop(head):
    prev = None
    curr = head
    # loop on current
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    # return new head prev
    return prev


# iterative Recursion
# value chnaged PREV, CURR put in parameters
# iterative code ruk kabb raha haii jab curr None Ho raha haii
# so curr None ho raha haii tab prev return kar rahe ho jo base
# case haii
def reverseSLLLoopRec(prev, curr):
    if curr is None:
        return prev
    # copy above iterative code
    # 1 case solve
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
    # recursion will handle
    return reverseSLLLoopRec(prev, curr)


prev = None
obj = SLL()
curr = obj.head
head = reverseSLL(prev, curr)
