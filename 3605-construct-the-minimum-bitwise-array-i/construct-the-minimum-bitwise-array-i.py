from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            found = False
            # Try all numbers from 0 to num to find the smallest x
            for x in range(num + 1):
                if x | (x + 1) == num:
                    ans.append(x)
                    found = True
                    break
            if not found:
                ans.append(-1)
        return ans
