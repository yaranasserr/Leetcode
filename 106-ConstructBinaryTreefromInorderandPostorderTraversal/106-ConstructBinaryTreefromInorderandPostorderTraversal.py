# Last updated: 5/30/2025, 7:54:54 PM
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
# build the right subtree first recusion n^2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder or not postorder:
            return None
        
        # Map each value to its index in inorder for O(1) lookup
        indices = {val: idx for idx, val in enumerate(inorder)}
        
        # Start from the end of postorder list (root of the tree)
        self.post_idx = len(postorder) - 1

        def dfs(left, right):
            if left > right:
                return None
            
            root_val = postorder[self.post_idx]
            self.post_idx -= 1

            root = TreeNode(root_val)
            mid = indices[root_val]

            # Build right subtree first
            root.right = dfs(mid + 1, right)
            root.left = dfs(left, mid - 1)

            return root

        return dfs(0, len(inorder) - 1)

# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
#         if not inorder or not postorder:
#             return None

#         root = TreeNode(postorder.pop())
#         mid = inorder.index(root.val)
#         root.left = self.buildTree(inorder[:mid],postorder)
#         root.right = self.buildTree(inorder[mid+1:],postorder)
        
#         return root 

#         # # Build the left and right subtrees recursively
#         # root.left = self.buildTree(inorder[:mid], postorder[:mid])
#         # root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
        
#         # return root

#O(n) solution
    # def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    #     # Create a dictionary to map each value in inorder to its index
    #     inorderIdx = {v: i for i, v in enumerate(inorder)}

    #     # Helper function to recursively build the tree
    #     def helper(left: int, right: int) -> Optional[TreeNode]:
    #         if left > right:
    #             return None
            
    #         # Pop the last value from postorder, which is the root
    #         root_val = postorder.pop()
    #         root = TreeNode(root_val)
            
    #         # Get the index of the root in the inorder traversal
    #         idx = inorderIdx[root_val]
            
    #         # Build the right subtree first (postorder is traversed from the end)
    #         root.right = helper(idx + 1, right)
            
    #         # Build the left subtree
    #         root.left = helper(left, idx - 1)
            
    #         return root
        
    #     # Initialize the recursive function with the bounds of the entire inorder list
    #     return helper(0, len(inorder) - 1)
