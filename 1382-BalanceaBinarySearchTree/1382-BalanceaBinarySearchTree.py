# Last updated: 2/9/2026, 10:08:02 AM
1class Solution(object):
2    def balanceBST(self, root):
3        """
4        :type root: Optional[TreeNode]
5        :rtype: Optional[TreeNode]
6        """
7        def inorder(node):
8            result = []
9            def dfs(n):
10                if not n:
11                    return
12                dfs(n.left)
13                result.append(n.val)
14                dfs(n.right)
15            dfs(node)
16            return result
17
18        arr = inorder(root)
19
20        def buildBST(l, r):
21            if l > r:
22                return None
23            mid = (l + r) // 2
24            node = TreeNode(arr[mid])
25            node.left = buildBST(l, mid - 1)
26            node.right = buildBST(mid + 1, r)
27            return node
28
29        return buildBST(0, len(arr) - 1)