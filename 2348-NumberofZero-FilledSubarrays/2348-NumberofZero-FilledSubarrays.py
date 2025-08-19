# Last updated: 8/19/2025, 3:26:23 PM
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt, streak = 0, 0
        for num in nums:
            if num == 0:
                streak += 1
                cnt += streak
            else:
                streak = 0
        return cnt