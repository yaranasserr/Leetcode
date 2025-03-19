# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         count =0 
#         for i in range(len(nums)-2):
#             while nums[i] == 0 :
#                 nums[i:i+3] = [x ^ 1   for x in nums[i:i+3]]
#                 print(nums)
#                 count +=1 

#         return count if all(x== 1 for x in nums) else -1  
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        
        for i in range(n - 2):  # Ensure we have at least 3 elements ahead
            if nums[i] == 0:
                # Flip the next three elements
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                count += 1

        return count if all(x == 1 for x in nums) else -1

        





        