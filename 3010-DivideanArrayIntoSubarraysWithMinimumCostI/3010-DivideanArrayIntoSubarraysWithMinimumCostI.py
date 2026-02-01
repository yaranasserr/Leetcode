# Last updated: 2/1/2026, 1:07:48 PM
1class Solution:
2    def minimumCost(self, nums: List[int]) -> int:
3        min1 = float('inf')
4        min2 = float('inf')
5        
6        for x in nums[1:]:
7            if x < min1:
8                min2 = min1
9                min1 = x
10            elif x < min2:
11                min2 = x
12                
13        return nums[0] + min1 + min2