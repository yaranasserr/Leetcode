# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        # Helper function to collect paths starting from the current node
        def dfs(root, current_sum, prefix_sums):
            if not root:
                return 0
            
            # Add the current node's value to the current sum
            current_sum += root.val
            
            # Count how many times (current_sum - targetSum) has occurred in the prefix sums
            count = prefix_sums.get(current_sum - targetSum, 0)
            
            # Add the current sum to the prefix sum dictionary
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
            # Recursively check the left and right subtrees
            count += dfs(root.left, current_sum, prefix_sums)
            count += dfs(root.right, current_sum, prefix_sums)
            
            # After finishing the recursion for this node, remove the current sum from the prefix sums
            prefix_sums[current_sum] -= 1
            
            return count
        
        # Start DFS with an initial sum of 0 and an empty prefix sum dictionary
        return dfs(root, 0, {0: 1})