'''
k groups reverse linked list
k = 3, 3-reverse

reverse k node first using loops
prev, curr, forward
after revarsal prev is head

head.next = rec ans

all linked list head return
prev

After Reversal
[prev]->[head]  [forward]->[]
prev is head so return
at end of LL head is pointed

Very very Important Question

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:

    def __init__(self):
        self.head = None
        self.tail = None

    def create_ll(self):
        first = Node(10)
        second = Node(20)
        third = Node(30)
        fourth = Node(40)
        fifth = Node(50)
        sixth = Node(60)
        self.head = first
        first.next = second
        second.next = third
        third.next = fourth
        fourth.next = fifth
        fifth.next = sixth
        self.tail = sixth

    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end='-')
            temp = temp.next
        print("\n")

    def getLength(self, head):
        lenDLL = 0
        temp = head
        while temp is not None:
            temp = temp.next
            lenDLL += 1
        return lenDLL

    def reverseKNodes(self, head, k):
        if head is None:
            print("LL is empty")
            return None
        lenLL = self.getLength(head)
        if k > lenLL:
            # print("Not valid K")
            return head
        # number of nodes in LL is greater than equal to K
        # step A - Reverse 1st K nodes of LL
        prev = None
        curr = head
        count = 0
        while count < k:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
            count += 1
        # step -B
        # aage bacha hua node attach karna haii
        if forward is not None:
            # we still have node left to reverse
            # aage node ka head forward
            # aage ka ans de dia self.reverseKNodes(forward, k)
            # connect to head ke next se
            head.next = self.reverseKNodes(forward, k)
        # step-c return head od modified linked list
        return prev


obj = SLL()
obj.create_ll()
obj.printLL()
obj.head = obj.reverseKNodes(obj.head, 6)
obj.printLL()
