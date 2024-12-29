# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder : [1,2,3,4,5,6]
        # inorder:[2,1,3,4]
        res=[]
        def dfs(node):
            if not node :
                return 
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            return res

        result=dfs(root)
        return(result[k-1])

        

        