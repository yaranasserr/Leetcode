# Last updated: 7/8/2025, 5:45:07 PM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%= len(nums)
        nums[:] = nums[-k:] +nums[:-k] 
  
        