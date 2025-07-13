# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # return lastnode in the level 
        q=deque([root])

        res = []
        while q :
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node :
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level :
                res.append(level[-1])

        return res 

        