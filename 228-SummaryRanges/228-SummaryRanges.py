# Last updated: 7/13/2025, 2:18:58 PM
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #dummy nodes pointing to the heads of these new lists.
        small_dummy = ListNode(0)
        big_dummy = ListNode(0)
        small = small_dummy
        big = big_dummy

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next

        big.next = None       
        small.next = big_dummy.next  # Connect the two partitions

        return small_dummy.next
