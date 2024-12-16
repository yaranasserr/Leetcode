# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # preorder : root , left , right 
        res = []
        def preorder(root):
            if not root:
                return 

            res.append("(")
            res.append(str(root.val))
            # handling empty left subtree but not null right subtree
            if not root.left  and root.right :
                res.append("()")

            preorder(root.left)
            preorder(root.right)
            res.append(")")

        preorder(root)

            
        return "".join(res)[1:-1] # eeminating the first and last ( )