'''
Q1. Is LL is Circular or Not
soln: go and check every node except head, its match with haed once come to head than circular
      you can use maps
      you can use slow and fast pointers

Q2: Detect and delete the Loops
 -> 8 type of soln exit
 # variation of question
 a. Loop present in Linked list
 b. starting point of Loops
 c. remove a Loops

 # Find Loop is present
 Approch1: address repeat again in loops using maps {key, val}
           key:address, val:bool(true, false)
           mark true initially
           if true is already there in map than loop is there
 Approch2: Floyd Cycle detection
        - slow, fast pointers
        - fast ko 2 step chalate haii than slow ko ek step chalate haii
        - jab vi fast and slow meet than Loop present
        - jab vi fast is NULL than loop not exit

# starting point of loops
- slow aur fast ko meet karwana
- slow ko hateo aur head pe lga do
- slow aur fast ko ek ek step chaleo
- slow fast meet than its starting points
proof:
head-startingpoint = A
slow and fast meet =  B
ciruclar dist = C
distance travelled by fast = 2* distance slow pointer
 A dist, multiple cycle , B distnce  = A + xC + B = Fast pointer
 Slow = A + yC + B
 A + xC + B = 2*(A + yC + B)
 (x-2y)C = A + B
 x-2y = k
 A + B = KC

 # Loop Remove
  - starting point se pahle wala pointer null kar do
  - fast ko aage vadha rahe the tabb prev pointer rakh lena
  - fast jab curr node pe hoga tabb prev pahle wala node pe hoga
  - prev.next = None

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
        seven = Node(70)
        eighth = Node(80)
        ninth = Node(90)
        self.head = first
        first.next = second
        second.next = third
        third.next = fourth
        fourth.next = fifth
        fifth.next = sixth
        sixth.next = seven
        seven.next = eighth
        eighth.next = ninth
        ninth.next = fifth
        self.tail = sixth

    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end='-')
            temp = temp.next
        print("\n")

    def checkForLoop(self):
        if self.head is None:
            return False
        slow = self.head
        fast = self.head
        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
                slow = slow.next
            if slow == fast:
                # loop present
                return True
        # loop se vhar nikalne pe fast Null ho gya
        # so loop not present
        return False

    def startingPoint(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
                slow = slow.next
            if slow == fast:
                slow = self.head
                break
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast

    def removeLoop(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
                slow = slow.next
            if slow == fast:
                slow = self.head
                break
        # 1 case me fatt jayega check it
        prev = fast
        while slow != fast:
            prev = fast
            slow = slow.next
            fast = fast.next
        prev.next = None
        return fast


obj = SLL()
obj.create_ll()
# obj.printLL()
print(obj.checkForLoop())
print(obj.startingPoint().data)
print(obj.removeLoop())
obj.printLL()
