# Last updated: 7/11/2025, 7:14:08 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head 

        # 1 -> 2 -> 3 ->4 ->5 
        # iterate till length - k -1 to reach the pivot node (3)
        # 1-2-3- null 4-5 ->head 
        # 4-5 -1 -2 3-null 
        length = 1
        tail = head # start
        while tail.next :
            tail = tail.next 
            length +=1

        k = k%length 
        if k == 0 :
            return head

        # reach the pivot 
        cur = head

        for i in range(length-k-1):
            cur = cur.next 

        new_head = cur.next # 4 
        cur.next = None # 3 points to None 

        tail.next = head # connect tail to the first node 
        return new_head

        





        