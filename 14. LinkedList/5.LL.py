'''

Find Middle of Linked List
- Even number of Nodes
  n//2 node is middle
- Odd number of Nodes
  n//2 + 1 is middle

soln: find length -> Even: Find n//2
                      Odd: Find n//2 + 1
TC: O(N) - 2 pass


Approch-2:
2-poiner approch/slow and fast pointer
-> fast 2 step aage ->
-> slow 1 step aage
Note: slow pointer tavi aage vadega
      jabb fast pointer 2 step aage vadd chuka hoga
Even: jab fast null pe pauchega to slow ko age karu ya na karu depend on question
ODD:
TC -> O(n), Single pass Approch


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
        self.head = first
        first.next = second
        second.next = third
        third.next = fourth
        fourth.next = fifth
        self.tail = fifth

    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end='-')
            temp = temp.next
        print("\n")

    def getMiddle(self):
        if self.head is None:
            print("empty")
            return self.head
        # if 1 node
        if self.head.next is None:
            return self.head
        # ll > 1 node
        slow = self.head
        # fast = self.head
        fast = self.head.next
        # work in even odd both case - self.head.next
        while slow is not None and fast is not None:
            # fast ko 2 step vadya
            fast = fast.next
            # 2 pointer aage edge cases handle
            if fast is not None:
                fast = fast.next
                # fast 2 step aage vadd gya
                # 1 step aage slow ko vada do
                slow = slow.next
        return slow


obj = SLL()
obj.create_ll()
obj.printLL()
x = obj.getMiddle()
print(x.data)
