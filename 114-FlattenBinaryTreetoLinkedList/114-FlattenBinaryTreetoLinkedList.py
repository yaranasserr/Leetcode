# Last updated: 7/29/2025, 8:48:09 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        # step 1: attach old right subtree after left subtree
        # step 2: move left subtree to right
        # step 3: set left to None
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node :
                return None

            lefttail = dfs(node.left) # last node in left subtree
            righttail = dfs(node.right)
            if node.left:
                lefttail.right = node.right
                node.right = node.left 
                node.left = None 

            last = righttail or lefttail or node


            return last 

        dfs(root)

   

        
        