# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
#         if not inorder or not postorder:
#             return None

#         root = TreeNode(postorder[-1])
      
#         mid = inorder.index(postorder[-1])

#         root.left = self.buildTree(postorder[1:mid+1],inorder[:mid])
#         root.right = self.buildTree(postorder[mid+1:],inorder[mid+1:])
#         return root 

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        # The root is the last element in postorder traversal
        root = TreeNode(postorder[-1])
        
        # Find the index of the root in inorder traversal
        mid = inorder.index(postorder[-1])

        # Build the left and right subtrees recursively
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
        
        return root
