# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         # reversing second part of linked list
#         # use fast andd slow pointer to find the middle  and reverse after it 
#         def reverse(head):
#             slow , fast = head , head 
#             while fast and fast.next :
#                 slow = slow.next
#                 fast=fast.next.next 
#         # the middle second subset of the list is in head 
#         # reverse the second subset
#             prev , curr = None , head
#             while curr:
#                 nxt = curr.next
#                 curr.next = prev
#                 prev = curr
#                 curr=nxt
#             return prev



#         middle = reverse(head)

#         pt1 = head 
#         pt2 = middle 

#         while head.next and middle.next:
#             themax  = max(pt1.val,pt2.val)
#         return themax


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Function to reverse a linked list
        def reverse(head):
            prev, curr = None, head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        # Step 1: Find the middle of the list using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        second_half = reverse(slow)

        # Step 3: Find the maximum twin sum
        max_twin_sum = 0
        first_half = head
        while second_half:
            max_twin_sum = max(max_twin_sum, first_half.val + second_half.val)
            first_half = first_half.next
            second_half = second_half.next

        return max_twin_sum
