'''
print kth node from end of Linked list

'''


def printFromEndLL(head):
    global ans
    global posFromTail
    if head is None:
        return
    printFromEndLL(head.next)
    # recursively aage vadhte jaeoge
    # end me last me pauch jaeoge
    # jab return karna tabb uss point pe posFromTail pe -- karte jaeo
    if posFromTail == 0:
        ans = head.data
    posFromTail -= 1
