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
        slow = head
        fast = head

        # Move fast k steps ahead
        for _ in range(k):
            fast = fast.next

        # Move both slow and fast until fast reaches the last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Step 4: Rotate the list
        new_head = slow.next
        slow.next = None  # Break the link
        fast.next = head  # Connect the tail to the original head

        return new_head
