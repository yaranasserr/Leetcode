# Last updated: 7/25/2025, 2:53:03 PM
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        else:
            return sum({x for x in nums if x >= 0})
