# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # bst tree , left < root , right > root for each tree
        if not head :
            return None 
        # root is the middle value  by slow and fast pointers 
        def middlenode(head):
            prev = None
            slow,fast = head , head

            while fast and fast.next :
                prev = slow 
                slow = slow.next
                fast = fast.next.next 

            # disconnect left half 
            if prev :
                prev.next = None

            return slow 

       
       
        
        def dfs(head): 
         
            if not head :
                return None
            mid= middlenode(head)
            root = TreeNode(mid.val)

            if mid == head :
                return root 

            root.left = dfs(head)
            root.right = dfs(mid.next)

            return root 
        return dfs(head)

            # if node.val < root.val :
            #     root.left = node.next 

            # if node.val > root.val :
            #     root.right = node.nect 

            # return root 

        

        

       

       

            
            

       
