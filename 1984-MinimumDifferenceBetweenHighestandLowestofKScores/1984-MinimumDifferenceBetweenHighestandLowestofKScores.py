# Last updated: 1/25/2026, 2:21:31 PM
1class Solution:
2    def minimumDifference(self, nums: List[int], k: int) -> int:
3        nums.sort()
4        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))