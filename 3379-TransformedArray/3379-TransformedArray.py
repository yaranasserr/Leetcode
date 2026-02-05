# Last updated: 2/5/2026, 5:17:04 PM
1class Solution:
2    def constructTransformedArray(self, nums):
3        n = len(nums)
4        return [nums[((i + nums[i]) % n + n) % n] for i in range(n)]