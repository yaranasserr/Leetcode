class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maximum = max(nums)
        return nums.index(maximum)