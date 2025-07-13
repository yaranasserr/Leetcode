# Last updated: 7/13/2025, 5:25:28 PM
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
        def dfs(root):
            if not root :
                return None 

            lefttail = dfs(root.left)
            righttail = dfs(root.right)

            if root.left :
                lefttail.right = root.right # connecting node 4 to top of node 5
                root.right = root.left # connecting 1 root to 2 node
                root.left = None 

            last = righttail or lefttail or root 

            return last 

        dfs(root)

        
        