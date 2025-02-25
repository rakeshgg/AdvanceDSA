'''
Next Greater Elemnts in Linked LIST
https://leetcode.com/problems/next-greater-node-in-linked-list/

You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node.
That is, for each node, find the value of the first node that is next
to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next
greater node of the ith node (1-indexed). If the ith node does not have
a next greater node, set answer[i] = 0.

Input: head = [2,1,5]
Output: [5,5,0]

Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]

SOLN:
elemnt se vada in right side
last elemnt next greater always zero

Approch1:
   two nested for loops - TC:O(n^2)
   for i in range(0, n)
    for j in range(i+1, n)
Approch2:
   - copy elemnts in LL array, working on array is easier
   -> ans arr to formed, save ith index ka next greater
   -> if decresing array ke bad koi vada ayage sabka Greater ho ga
   - agar monotoically decresing array bna lu -> Jaise koi vada aya
   # indexes inside stack
   if ll[i] > stack_top
      # stack me jitne elemnts haii unn sabka greater elemnts ll[i] Hoge
      # pop till stack top < ll[i] and rill greater
   else:
      st.push(i)


'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def nextLargerNodes(head):
    ll = []
    while head:
        ll.append(head.val)
        head = head.next
    # stack
    st = []
    ans = [0] * len(ll)
    for i in range(len(ll)):
        while not len(st) and ll[i] > ll[st[-1]]:
            # means ith elements is the next greater elemnts present
            kids = st.pop()
            ans[kids] = ll[i]
        st.push(i)
    return ans
