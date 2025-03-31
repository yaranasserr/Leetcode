# Last updated: 3/31/2025, 5:13:05 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def gen(left,right):
            if left == right :
                return [TreeNode(left)]

            if left > right :
                return [None]

            res = []
            #any val can be the root 
            for val in range(left,right+1):
                root =TreeNode(val)

                for lefttree in gen(left,val-1): # left subtree 
                    for righttree in gen(val+1,right):
                        root = TreeNode(val,lefttree,righttree)
                        res.append(root)

            return res



        return gen(1,n)


        