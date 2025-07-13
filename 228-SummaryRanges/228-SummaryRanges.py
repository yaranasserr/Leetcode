# Last updated: 7/13/2025, 4:03:56 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val:idx for idx,val in enumerate(inorder)}

        self.preidx= 0 # idx for root in preorder 
        def dfs(l,r):
            if l > r :
                return None 

            root_val = preorder[self.preidx]
            self.preidx+=1 
            root = TreeNode(root_val)
            # Find the index of this root in inorder to split left and right subtrees
            mid = indices[root_val]
            root.left=dfs(l,mid-1)
            root.right=dfs(mid+1,r)

            return root 

        return dfs(0,len(inorder)-1)
        