# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head) # value , next pointer : points to head 

        leftprev = dummy # empty node 
        cur = head 
        # prev: node before left  node
        # cur on left node 

        for i in range(left-1):
            leftprev = cur 
            cur = cur.next 

        prev = None 
        # reverse 

        for i in range(right - left +1):
            nxt = cur.next 
            cur.next = prev
            prev = cur
            cur = nxt 

        leftprev.next.next = cur  # pointer of the node aafter leftprev = node after right 
        leftprev.next = prev  # prev is right


        return dummy.next


        
        