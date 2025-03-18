from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0  
        mask = 0  # Bitmask to store OR of elements in the window
        res = 0  

        for r in range(len(nums)):
            # If adding nums[r] causes a conflict, shrink the window
            while (mask & nums[r]) != 0:
                mask ^= nums[l]  # Remove nums[l] from the mask
                l += 1  # Move left pointer
            
            # Include nums[r] in the window
            mask |= nums[r]
            res = max(res, r - l + 1)  # Update the max length
        
        return res
