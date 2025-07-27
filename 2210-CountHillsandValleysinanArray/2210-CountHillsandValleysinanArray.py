# Last updated: 7/27/2025, 2:30:29 PM
from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # remove consecutive duplicates
        clean = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                clean.append(nums[i])

        hills, valleys = 0, 0
        for i in range(1, len(clean) - 1):
            if clean[i - 1] < clean[i] > clean[i + 1]:
                hills += 1
            elif clean[i - 1] > clean[i] < clean[i + 1]:
                valleys += 1

        return hills + valleys
