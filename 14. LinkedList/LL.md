# Linked List
- dymicaly grow shrink at runtime
- none continous memory allocation/westage of memory nahi hota haii
- concept of addresses

# DEF
A collections of Nodes attached in Linear Form - har node ka descendent node haii
Node: [data, address]
address -> next node ka
SLL - Single Linked List
CLL - Circular Singly Linked List
DLL - Doubly Linked List
CDLL - Circular Doubly Linked List

# Linked List
STEP A: maggi ka paket fad do
STEP B: Panni Garam Kar lo
STEP C: Maggi Pani me Dal do
???????
LL is Hindi



class Node:
    def __init__(self, data):
        "constructor class to initiate this object"

        # store data
        self.data = data
        
        # store reference (next item)
        self.next = None

        # store reference (previous item)
        # used in DLL
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


# circular singly LL
sLL -> head, tail
tail.next = head -> circular
circular me -> no head, no tail, insert, del, based on value

# circular Doubly LL
tail.next = head
head.prev = tail
circular me -> no head, no tail, insertion, deletion, based on value
