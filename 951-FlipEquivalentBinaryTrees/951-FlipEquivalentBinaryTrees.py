# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
class Solution:
    def flipEquiv(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        if not r1 or not r2 :
            return not r1 and not r2 

        if r1.val != r2.val:
            return False

        a= self.flipEquiv(r1.left,r2.left) and self.flipEquiv(r1.right,r2.right)
        # if false flip them 

        return a or self.flipEquiv(r1.left,r2.right) and self.flipEquiv(r1.right,r2.left)





        

#         def invertTree(root):
#             if not root:
#                 return None
#             inverted_root = TreeNode(root.val)
#             inverted_left = invertTree(root.left)
#             inverted_right = invertTree(root.right)
#             return inverted_root

#         def isSame(root1,root2):
#             if not root1 and not root2:
#                 return True 
#             if not root1 or root2 :
#                 return False
            
#             return (root1.val == root2.val and isSame(root1.left,root2.left) and isSame(root1.right,root2.right))

#         inverted_tree2=invertTree(root2)

#         return isSame(root1,inverted_tree2)

        


