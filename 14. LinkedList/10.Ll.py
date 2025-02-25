'''
Sort 0's, 1's and 2's

Approch1:
- count 0's, 1's, 2's
- Traverse LL and put 0's, 1's, 2's
counting + replacements -> O(n)

Approch2: data replacement not allowed
 # isolated First Node
 - temp = head
 - head = head.next
 - temp.next = None
 # 3 linked list make haivng 0's, 1's, 2's
 - Join linked list
 - remove dummy nodes
 - return head

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
        first = Node(1)
        second = Node(2)
        third = Node(2)
        fourth = Node(0)
        fifth = Node(0)
        sixth = Node(0)
        # seven = Node(70)
        # eighth = Node(80)
        # ninth = Node(90)
        self.head = first
        first.next = second
        second.next = third
        third.next = fourth
        fourth.next = fifth
        fifth.next = sixth
        # sixth.next = seven
        # seven.next = eighth
        # eighth.next = ninth
        # ninth.next = None
        self.tail = sixth

    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end='->')
            temp = temp.next
        print("\n")

    def sortZeroOneTwo(self):
        # using data Replacemnts
        # step 1 find count of 1's zero
        zero = 0
        one = 0
        two = 0
        temp = self.head
        while temp is not None:
            if temp.data == 0:
                zero += 1
            elif temp.data == 1:
                one += 1
            elif temp.data == 2:
                two += 1
            temp = temp.next
        # fill ones, zero in original list
        temp = self.head
        while temp is not None:
            # fill zero
            while zero:
                temp.data = 0
                temp = temp.next
                zero -= 1
            # fill one
            while one:
                temp.data = 1
                temp = temp.next
                one -= 1
            # fill two
            while two:
                temp.data = 2
                temp = temp.next
                two -= 1

    def sortZeroOnesTwo2(self):
        # linked list empty
        if self.head is None:
            return
        if self.head.next is None:
            return
        # create dummy nodes
        zeroHead = Node(-1)
        zerotail = zeroHead
        oneHead = Node(-1)
        onetail = oneHead
        twoHead = Node(-1)
        twotail = twoHead
        # traverse the original LL
        curr = self.head
        while curr is not None:
            if curr.data == 0:
                # node ko utha ke zero head linked list me dalna haii
                temp = curr
                curr = curr.next
                temp.next = None
                # seperated zero node
                # append the zero node in zero head LL
                zerotail.next = temp
                zerotail = temp
            elif curr.data == 1:
                # node ko utha ke zero head linked list me dalna haii
                temp = curr
                curr = curr.next
                temp.next = None
                # seperated zero node
                # append the zero node in zero head LL
                onetail.next = temp
                onetail = temp
            elif curr.data == 2:
                # node ko utha ke zero head linked list me dalna haii
                temp = curr
                curr = curr.next
                temp.next = None
                # seperated zero node
                # append the zero node in zero head LL
                twotail.next = temp
                twotail = temp
        # join 3 list
        # remove dummy linked list
        # return new head
        temp = oneHead
        oneHead = oneHead.next
        # remove dummy node
        temp.next = None
        # modify two wali list
        temp = twoHead
        twoHead = twoHead.next
        # remove dummy node
        temp.next = None
        # join list
        if oneHead is not None:
            # one list is non empty
            zerotail.next = oneHead
            if twoHead is not None:
                onetail.next = twoHead
        else:
            # one wali list is empty
            if twoHead is not None:
                zerotail.next = twoHead
        # remove zero head dummy node
        temp = zeroHead
        zeroHead = zeroHead.next
        temp.next = None
        self.head = zeroHead
        return


obj = SLL()
obj.create_ll()
obj.printLL()
# obj.sortZeroOneTwo()
obj.sortZeroOnesTwo2()
obj.printLL()
