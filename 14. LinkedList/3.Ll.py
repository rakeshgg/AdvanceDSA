'''
Doubly Linked List


'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="<->")
            temp = temp.next
        print("\n")

    def getLength(self):
        lenDLL = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            lenDLL += 1
        return lenDLL

    def inserAtHead(self, data):
        '''
        A. create a newNode
        B. newNode.next = head
        c. head.prev = newNode
        D. head = newNode
        - Handle Empty case

        '''
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode
        else:
            # non empty case
            newNode = Node(data)
            # step 2
            newNode.next = self.head
            # step 3
            self.head.prev = newNode
            self.head = newNode

    def inserAtTail(self, data):
        '''
        A. create a newNode
        B. tail.next = newNode
        c. newNode.prev = tail
        D. tail = newNode
        - Handle Empty case

        '''
        if self.head is None:
            # linked list Empty
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode
        else:
            # non empty case
            newNode = Node(data)
            # step 2
            self.tail.next = newNode
            # step 3
            newNode.prev = self.tail
            self.tail = newNode

    def insertATposition(self, data, pos):
        '''
        pos can be anything
        find prevnode and curr
        create a node
        prev.next = newnode
        newnode.prev = prevnode
        curr.prev = newnode
        newnode.next = curr
        '''
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode
        else:
            # LL is not empty
            if pos == 1:
                self.inserAtHead(data)
            lenDLL = self.getLength()
            if pos > lenDLL:
                # insert at last
                self.inserAtTail(data)
            # insert at middle
            # ste find prev and curr depend on position
            i = 1
            prevNode = self.head
            while i < pos-1:
                prevNode = prevNode.next
                i += 1
            curr = prevNode.next
            # curr node can't be null as last node is
            # already handled
            newNode = Node(data)
            # step-3 - order not matter in prev, curr pointer
            # if curr pointer only than order matters
            prevNode.next = newNode
            newNode.prev = prevNode
            curr.prev = newNode
            newNode.next = curr

    def deleteATposition(self, pos):
        # empty case
        if self.head is None:
            print('Linked list is Empty')
            return
        # single node
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        if pos == 1:
            # delete first Node
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            return
        lenDLL = self.getLength()
        if pos >= lenDLL:
            # delete last node
            temp = self.tail
            self.tail = self.tail.prev
            temp.prev = None
            self.tail.next = None
            return
        # delete from middle of linked list
        # find left, curr, right
        left = self.head
        i = 1
        while i < pos - 1:
            left = left.next
            i += 1
        curr = left.next
        right = curr.next
        # step - 2
        left.next = right
        # step - 3
        right.prev = left
        # step - 4
        curr.next = None
        curr.prev = None


if __name__ == '__main__':
    first = Node(10)
    second = Node(20)
    third = Node(30)

    first.next = second
    second.prev = first

    second.next = third
    third.prev = second
    obj = DoublyLL()
    obj.head = first
    obj.tail = third
    obj.printLL()
    obj.inserAtHead(110)
    obj.printLL()
    obj.inserAtTail(220)
    obj.printLL()
    obj.insertATposition(2011, 5)
    obj.printLL()
    obj.deleteATposition(3)
    obj.printLL()
