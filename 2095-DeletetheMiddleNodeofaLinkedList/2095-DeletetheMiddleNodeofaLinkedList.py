# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Solve by two pointers
        if not head or not head.next:  # Edge case: single node or empty list
            return None 
        
        slow, fast = head, head
        prev = None  # Keep track of the node before `slow`
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Remove the middle node
        prev.next = slow.next
        
        return head
