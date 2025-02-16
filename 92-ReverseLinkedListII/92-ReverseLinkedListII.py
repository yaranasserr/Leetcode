# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # get the pointer to the left 
        dummy = ListNode(0,head)
        leftprev , cur = dummy,head 
        for i in range(left-1):
            leftprev , cur = cur , cur.next 

        # reversing 
        prev = None 
        for i in range(right-left+1):
            nxt= cur.next 
           
            cur.next = prev
            prev , cur = cur ,nxt 

        # connecting the reversed nodes to original nodes 
        leftprev.next.next = cur 
        leftprev.next = prev 

        return dummy.next
    
        