# Last updated: 7/30/2025, 1:18:34 PM
from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        max_level = 0
        level = 1
        
        q = deque([root])
        
        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
                
            level += 1
        
        return max_level
