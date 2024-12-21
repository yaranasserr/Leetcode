# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True  # An empty tree is symmetric

        def dfs(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if not t1 and not t2:
                return True  
            if not t1 or not t2:
                return False  # One subtree is empty, the other is not, not symmetric
            # Check if the values are equal and recursively check for symmetry in children
            return (t1.val == t2.val) and dfs(t1.left, t2.right) and dfs(t1.right, t2.left)

        return dfs(root.left, root.right)
