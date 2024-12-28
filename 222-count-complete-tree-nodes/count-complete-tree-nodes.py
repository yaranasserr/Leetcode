# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        res = []
        q= collections.deque()
        q.append(root)

        while q :
            qlen= len(q)
            level = []
            for i in range(qlen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:

                res.append(level)
        flattened_list = [item for sublist in res for item in sublist]
        return (len(flattened_list))
        