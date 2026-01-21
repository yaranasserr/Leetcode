# Last updated: 1/21/2026, 1:58:28 PM
1class Solution:
2    def minBitwiseArray(self, nums: List[int]) -> List[int]:
3        for i in range(len(nums)):
4            res = -1
5            d = 1
6            while (nums[i] & d) != 0:
7                res = nums[i] - d
8                d <<= 1
9            nums[i] = res
10        return nums