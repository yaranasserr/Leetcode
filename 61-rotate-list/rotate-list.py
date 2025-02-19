from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length of the linked list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Compute the effective rotations needed
        k = k % length
        if k == 0:
            return head

        # Step 3: Use two-pointer technique
        cur = head 
      
        # Move fast k steps ahead
        for i in range(length-k-1):
            cur = cur.next 
        new_head=cur.next
        cur.next = None

        # be the beginning
        tail.next = head 
        return new_head

 
