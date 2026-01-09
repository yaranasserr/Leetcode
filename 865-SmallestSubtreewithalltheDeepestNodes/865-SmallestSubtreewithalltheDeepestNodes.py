# Last updated: 1/9/2026, 3:18:37 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def subtreeWithAllDeepest(self, r: Optional[TreeNode]) -> Optional[TreeNode]:
9        def f(n):
10            if not n: return 0,None
11            ld,ln,rd,rn = *f(n.left),*f(n.right)
12            return ((ld+1,n),(ld+1,ln),(rd+1,rn))[(ld>rd)-(ld<rd)]
13
14        return f(r)[1]