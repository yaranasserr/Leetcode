# Last updated: 1/20/2026, 12:42:07 PM
1from typing import List
2
3class Solution:
4    def minBitwiseArray(self, nums: List[int]) -> List[int]:
5        ans = []
6        for num in nums:
7            found = False
8            # Try all numbers from 0 to num to find the smallest x
9            for x in range(num + 1):
10                if x | (x + 1) == num:
11                    ans.append(x)
12                    found = True
13                    break
14            if not found:
15                ans.append(-1)
16        return ans
17