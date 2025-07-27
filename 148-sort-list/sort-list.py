# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Use slow & fast pointers to find the midpoint.

# Cut the list into two halves.

# Recursively sort both halves.

# Merge the two sorted halves using a dummy node.

# Time Complexity: O(n log n)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if list is empty or has only one node, it's already sorted
        if not head or not head.next:
            return head

        # Split the list into two halves using slow and fast pointer
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Cut the list into two halves
        prev.next = None

        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge(left, right)

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        # Append the remaining nodes
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return dummy.next
