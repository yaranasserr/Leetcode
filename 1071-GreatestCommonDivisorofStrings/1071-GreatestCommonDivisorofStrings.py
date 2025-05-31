# Last updated: 5/31/2025, 11:49:52 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        side = []

        q = deque([root])

        while q :
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node :
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level :
                side.append(level[-1])

        return side



























        
        # res = []
        # q=collections.deque([root])

        # while q :
        #     rightSide=None
        #     qLen = len(q) # length of current level only 
        #     for i in range(qLen):
        #         node = q.popleft()
        #         if node :
        #             rightSide = node 
        #             q.append(node.left)
        #             q.append(node.right)

        #     if rightSide:
        #         res.append(rightSide.val)
        # return res

        