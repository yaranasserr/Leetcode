# Last updated: 1/7/2026, 12:55:33 PM
1class Solution:
2    def maxProduct(self, root: Optional[TreeNode]) -> int:
3        MOD = 10**9 + 7
4
5        def dfs(node):
6            if not node:
7                return 0
8            
9            node.val += dfs(node.left) + dfs(node.right)
10            return node.val
11
12        total = dfs(root)
13
14        ans = 0
15        q = deque([root])
16
17        while q:
18            node = q.popleft()
19            if not node:
20                continue
21
22            
23            current_product = (total - node.val) * node.val
24            ans = max(ans, current_product)
25
26            if node.left:
27                q.append(node.left)
28            if node.right:
29                q.append(node.right)
30
31        return ans % MOD