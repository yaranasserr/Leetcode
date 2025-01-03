# class Solution:
#     def waysToSplitArray(self, nums: List[int]) -> int:
#         sumleft = 0 
#         sumright = 0
#         count = 0

#         for i in range(len(nums)):
#             sum_left = sum(nums[:i])
          
#             sum_right = sum(nums[i:])
          
#             if sum_left >= sum_right :
#                 count +=1 

#         return count 

from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Total sum of the array
        sum_left = 0
        count = 0
        
        # Iterate through the array until the second-to-last element
        for i in range(len(nums) - 1):
            sum_left += nums[i]  # Incrementally build the left sum
            sum_right = total_sum - sum_left  # Calculate the right sum
            
            if sum_left >= sum_right:
                count += 1
                
        return count
            

        