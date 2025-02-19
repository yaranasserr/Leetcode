# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy =ListNode(0,head)
        prev = dummy # before duplicates  
        cur = head
        while cur :
            
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val :
                    cur= cur.next 
                prev.next = cur.next # connect prev to next unique node 
            else :
                prev = prev.next  # move prev forward if no dupliacates
            cur = cur.next  # move cur forward 

        return dummy.next
                    
                
            