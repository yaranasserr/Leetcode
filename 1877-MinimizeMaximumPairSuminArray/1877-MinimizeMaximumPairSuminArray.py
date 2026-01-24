# Last updated: 1/24/2026, 12:37:12 PM
1from typing import List
2
3class Solution:
4    def minPairSum(self, nums: List[int]) -> int:
5        nums.sort()
6        
7        max_sum = 0
8        n = len(nums)
9        
10        for i in range(n // 2):
11            max_sum = max(max_sum, nums[i] + nums[n - 1 - i])
12        
13        return max_sum
14