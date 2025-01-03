# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # return [ withroot, without root]
        def dfs(root):
            if not root:
                return [0,0]

            leftPair = dfs(root.left)
            rightPair = dfs(root.right)
            withroot = root.val +leftPair[1] +rightPair[1]
            withoutRoot = max(leftPair) + max(rightPair)

            return [withroot , withoutRoot]

        return max(dfs(root))

  

        