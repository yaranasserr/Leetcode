class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # First, find the start index of the target
        start = -1
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                break  # exit loop once start is found
        
        # If target is not found, return [-1, -1]
        if start == -1:
            return [-1, -1]
        
        # Now find the end index of the target
        end = start
        while end + 1 < len(nums) and nums[end + 1] == target:
            end += 1
        
        return [start, end]
