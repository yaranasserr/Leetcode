# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        # sorted = {5:0,6:1,7:2,8:3}
        # unsorted = {7:0 , 6:1,8:2,5:3}
        #7 (index 0) → 7 belongs at index 2
        # 8 (index 2) → 8 belongs at index 3
        # 5 (index 3) → 5 belongs at index 0

        def count_swaps(nums):
            swaps = 0 
            sorted_nums=sorted(nums)
            # unsorted dict
            idx ={n:i for i , n in enumerate(nums)}
            for i in range(len(nums)):
                if nums[i] != sorted_nums[i]:
                    swaps+=1
                    # do swap 
                    # the unsorted index
                    j = idx[sorted_nums[i]]
                    nums[i],nums[j] = nums[j],nums[i]
                    idx[nums[j]] = j 

            return swaps 

        q= deque([root])
        swaps = 0
        while q :
            level=[]
            for i in range(len(q)):
                node = q.popleft()
                
                if node :
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level :
                swaps+=count_swaps(level)

        return swaps









            
        