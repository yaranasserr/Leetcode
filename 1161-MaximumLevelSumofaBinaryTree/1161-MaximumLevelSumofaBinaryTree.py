# Last updated: 1/6/2026, 11:09:34 AM
1from collections import deque
2
3class Solution:
4    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
5        max_sum = float('-inf')
6        max_level = 0
7        level = 1
8        
9        q = deque([root])
10        
11        while q:
12            level_sum = 0
13            for _ in range(len(q)):
14                node = q.popleft()
15                level_sum += node.val
16                if node.left:
17                    q.append(node.left)
18                if node.right:
19                    q.append(node.right)
20            
21            if level_sum > max_sum:
22                max_sum = level_sum
23                max_level = level
24                
25            level += 1
26        
27        return max_level
28