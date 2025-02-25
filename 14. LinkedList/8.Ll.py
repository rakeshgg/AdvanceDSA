'''
check Linked list is Palindrome or not
- Right se left read or read from left to right is same than Palindrome
Soln:
- create new linked list reverse of aobove linked list - TC: O(n), SC:O(n)
- Reverse from Mid and check, in array two pointer start, end

3rd approch:
copy data of LL in array apply array Logic, space-> O(n)

# in O(1) - Space-Approch
 - Reverse LL from middle, using slow, fast pointer
 - Reverse LL after middle node
 - compare temp1, and temp2(reverse one)/Compare both halves
 TC: O(N), SC:O(1)

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
        fourth = Node(20)
        fifth = Node(10)
        # sixth = Node(60)
        # seven = Node(70)
        # eighth = Node(80)
        # ninth = Node(90)
        self.head = first
        first.next = second
        second.next = third
        third.next = fourth
        fourth.next = fifth
        # fifth.next = sixth
        # sixth.next = seven
        # seven.next = eighth
        # eighth.next = ninth
        # ninth.next = None
        self.tail = fifth

    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end='-')
            temp = temp.next
        print("\n")

    def reverseLL(self, head):
        prev = None
        curr = head
        next = curr.next
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def checkPalindrome(self):
        if self.head is None:
            print("Empty List")
            # check with interviwer either want to return True ot False
            return True
        # single Node
        if self.head.next is None:
            return True
        # > 1 Node
        # step-A Find the middle node
        slow = self.head
        fast = self.head.next
        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
                slow = slow.next
        # slow pointer is pointing to middle node
        # step-B reverse Linked List after middle Node
        reverseLLHead = self.reverseLL(slow.next)
        # join the reversed LL in Left part, Join is not Important
        slow.next = reverseLLHead
        # step-c start comparison
        temp1 = self.head
        temp2 = reverseLLHead
        while temp2 is not None:
            if temp1.data != temp2.data:
                # not a palindrome
                return False
            else:
                # if equal
                temp1 = temp1.next
                temp2 = temp2.next
        return True


obj = SLL()
obj.create_ll()
obj.printLL()
isPalindrome = obj.checkPalindrome()
print(isPalindrome)
obj.printLL()
