from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2  
            
            if nums[mid] == target:  # Target found
                return mid
            elif nums[mid] < target:  # Target is greater, move to the right half
                l = mid + 1
            else:  # Target is smaller, move to the left half
                r = mid - 1
        
        # l points to the smallest index where the target could be inserted to maintain the sorted order.
        return l
