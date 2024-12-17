# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow pointer for odd , fast pointer for even 
        if not head:
            return None 

        slow = head
        fast = even_head= head.next 

        while fast and fast.next :
            slow.next = slow.next.next
            slow=slow.next
            fast.next=fast.next.next
            fast=fast.next 
            
        slow.next = even_head
        return head 
            # connect tail of the odd with the head of even 

        return head
        