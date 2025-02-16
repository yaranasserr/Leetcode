# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupprev = dummy 
        while True :
            kth = self.getkth(groupprev,k)
            if not kth :
                break
            groupnext = kth.next

            # reverse group 
            prev , curr = kth.next , groupprev.next 
            while curr != groupnext :
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupprev.next 
            groupprev.next = kth 
            groupprev = tmp

        return dummy.next 
    def getkth(self,curr,k):
        while curr and k >0 :
            curr = curr.next 
            k-=1 
        return curr




        # def get_length_recursive(head: ListNode) -> int:
        #     if not head:
        #         return 0
        #     return 1 + get_length_recursive(head.next)

        # length = get_length_recursive(head)
        # leftoutnodes = length% k 
        # groups= length//k 
        # # do the loop no of groups times 
        # # reverse each k nodes alone then connect 
        # dummy = ListNode(0,head)
        # def reverse(head):
        #     prev , cur = dummy , head 
        #     while cur :
        #         #reverse k nodes 
        #         nxt = cur.next 
        #         cur.next = prev 
        #         prev = cur 
        #         cur = nxt 
        #     return prev 

        # for i in range(groups):
        #     for node in range(k):
        #         reverse(head)

        # # connecting the revrsed sublists together 






                