# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
           
# maximum zigzag given a node and direction (right or left).
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 

        max_length = 0 

        def dfs(node,is_left,length):
            nonlocal max_length 
            if not node :
                return 

            max_length = max(max_length , length)
            if is_left:
                dfs(node.left,False,length+1) # next time go right
                dfs(node.right,True,1) # new start node
            else:
                dfs(node.right,True,length+1) # next time go left 
                dfs(node.left,False,1) # new start node


        dfs(root,True,0) 

        return max_length
            #if it goes true go left , false go right 




 
        