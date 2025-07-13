# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indices = {val:idx for idx,val in enumerate(inorder)}
        self.ptr = len(postorder)-1

        def dfs(left,right):
            if left> right:
                return None
            root_val=postorder[self.ptr]
            self.ptr-=1

            root=TreeNode(root_val)
            mid=indices[root_val]

            root.right=dfs(mid+1,right)
            root.left=dfs(left,mid-1)

            return root

        return dfs(0,len(postorder)-1)
        