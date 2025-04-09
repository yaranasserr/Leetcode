# Last updated: 4/9/2025, 2:53:35 PM
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = set(nums)  
        if nums == {k}:  
            return 0
        
       
        if any(num < k for num in nums):
            return -1
        
        ops = 0
        for num in nums:
            if num > k:
                ops += 1
        
        return ops if ops != 0 else -1
