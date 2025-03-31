# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # from beginning :left
        cur = head
    
        for i in range(k-1):
            cur = cur.next 
        
        left = cur 
        right = head

        # distance btween start , l = dis bet r and end
        while cur.next:
            cur=cur.next
            right = right.next

        left.val , right.val = right.val , left.val

        return head

        