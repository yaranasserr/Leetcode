# Last updated: 7/24/2025, 4:54:36 PM
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(cur, num):
            if not cur:
                return 0  # Return 0 for null nodes
            num = num * 10 + cur.val
            if not cur.left and not cur.right:  # Proper leaf node check
                return num
            # Sum the numbers from left and right subtrees
            return dfs(cur.left, num) + dfs(cur.right, num)

        return dfs(root, 0)