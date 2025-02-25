'''
LL Creation

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printLL(head):
    '''
    1. Print kardo data
    2. pointer ko aage le jaeo
    3. ruko jab pointer null ho
    '''
    temp = head
    while temp is not None:
        print(temp.data, end='-')
        temp = temp.next


def insertAtHead(head, tail, data):
    '''
    Insert infront of linked list
    - create newnode
    - node ko attach karo
    - head update kar do
    '''
    # check for empty LL
    if head is None:
        newNode = Node(data)
        head = newNode
        tail = newNode
        return head, tail
    # step1
    newNode = Node(data)
    # step2
    newNode.next = head
    # step3
    head = newNode
    return head, tail


def insertAtTail(head, tail, data):
    '''
    Insert end of linked list
    - create newnode
    - node ko attach karo
    - tail update kar do
    '''
    if head is None:
        newNode = Node(data)
        head = newNode
        tail = newNode
        return head, tail
    # step1 - create a node
    newNode = Node(data)
    # step2 - connect with tail node
    tail.next = newNode
    # newNode.next = head
    # step3 - update tail
    tail = newNode
    return head, tail


def findLendth(head):
    lenLL = 0
    temp = head
    while temp is not None:
        lenLL += 1
        temp = temp.next
    return lenLL


def inserAtPosition(head, tail, data, pos):
    '''
    Either position or vale given uske bad
    we are doing on position
    -> Empty Game
    -> Non-Empty Game
       1. Find that Position
          Prev, Curr ke bich me dalna haii
       2. create a node
       new node next ko current pe laga dia
       prev ke next me new node pointer dal dia
    '''
    if head is None:
        newNode = Node(data)
        head = newNode
        tail = newNode
        return head, tail
    # step 1 Find the position prev, curr pointer
    if pos == 0:
        return insertAtHead(head, tail, data)
    lenLL = findLendth(head)
    # insert at END
    if pos >= lenLL:
        return insertAtTail(head, tail, data)
    i = 1
    prev = head
    while i < pos:
        prev = prev.next
        i += 1
    curr = prev.next
    # step 2
    newNode = Node(data)
    # step 3
    newNode.next = curr
    # step 4
    prev.next = newNode
    return head, tail


def delete(head, tail, pos):
    '''
    delete front, middle, end
    Empty/ NonEmpty Case
    head and Tail Update

    Delete First
    - update head to next node
    - temp.next = None

    Delete Last Node
    - Tail pixe nahi le ja sakte
    - Iterate through last node and store PREV during iteration
    - Prev Find
    - prev.next = None
    - update tail
    - delete Temp

    '''
    if head is None:
        print("cannot delete empty")
        return head, tail
    if pos == 1:
        temp = head
        head = head.next
        temp.next = None
        return head, tail
    lenLL = findLendth(head)
    # at end of linked list
    if pos == lenLL:
        # find prev
        prev = head
        i = 1
        while i < pos-1:
            prev = prev.next
            i += 1
        prev.next = None
        tail = prev
        return head, tail
    # middle position
    # need to delete curr one
    # find prev and curr
    # prev.next = curr.next
    # curr.next = None
    i = 1
    prev = head
    # pos-1 ek pahle wala node pe jana haii
    while i < pos-1:
        prev = prev.next
        i += 1
    curr = prev.next
    prev.next = curr.next
    curr.next = None
    return head, tail


if __name__ == '__main__':
    # jab vi head aur tail ko initialize kare ho
    # aap ko head aur tail se unn dono node ko
    # initialize karna padega
    head = None
    tail = None
    head, tail = insertAtHead(head, tail, 20)
    head, tail = insertAtHead(head, tail, 30)
    head, tail = insertAtHead(head, tail, 40)
    head, tail = insertAtHead(head, tail, 50)
    head, tail = insertAtHead(head, tail, 60)
    # printLL(head)
    head, tail = insertAtTail(head, tail, 70)
    head, tail = insertAtTail(head, tail, 80)
    head, tail = insertAtTail(head, tail, 90)
    head, tail = insertAtTail(head, tail, 100)
    # printLL(head)
    head, tail = inserAtPosition(head, tail, 101, 9)
    printLL(head)
    print("\n")
    head, tail = delete(head, tail, 6)
    printLL(head)
