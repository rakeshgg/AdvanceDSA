# n = size(nodes)

'''
# before: 1-2-3-4-5-6-7
def traverse(head: ListNode) -> None:
    if not head: return 
    slow, fast, dummy = head, head, ListNode(0, head)
    # puts slow in the middle
    while fast and fast.next:
        slow = slow.next;
        fast = fast.next.next;
    #        d h     s     f
    # after: 0-1-2-3-4-5-6-7

'''