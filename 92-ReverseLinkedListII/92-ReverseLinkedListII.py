# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases where the head might change
        dummy = ListNode(0, head)
        
        # Initialize pointers to traverse to the `left` position
        leftprev, cur = dummy, head
        for i in range(left - 1):
            leftprev, cur = cur, cur.next  # Move both pointers forward
        
        # Reverse the sublist from `left` to `right`
        prev = None
        for i in range(right - left + 1):
            nxt = cur.next  # Store the next node
            cur.next = prev  # Reverse the current node's pointer
            prev, cur = cur, nxt  # Move forward in the list

        # Connect the reversed sublist with the original list
        leftprev.next.next = cur  # Connect the tail of reversed sublist to remaining list
        leftprev.next = prev  # Connect the start of reversed sublist to previous part

        return dummy.next  # Return the new head of the list
