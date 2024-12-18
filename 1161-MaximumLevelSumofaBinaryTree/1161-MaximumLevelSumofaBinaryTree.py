# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        res = []
        q=collections.deque()
        q.append(root)
        while q:
            qLen = len(q) #iterate through one level
            level=[]
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:

                res.append(level)
        max_index = max(range(len(res)), key=lambda i: sum(res[i]))
        return(max_index + 1)



        

        