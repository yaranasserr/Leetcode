# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head) # value , pointer 
        left = dummy  # pointer 
        right = head # pointer 
        # start right with distance n from left 

        while n > 0 and right :
            right = right.next 
            n-=1
        # shift right and left  till right is out of bounds
        while right :
            left = left.next
            right = right.next

        # delete the node
        # now left is pointing to node before the to be deleted node
        left.next = left.next.next
        return dummy.next



        

        
        