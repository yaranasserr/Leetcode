# Last updated: 5/30/2025, 10:37:50 PM
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        groups = []  # List of lists to hold number groups
        group = [nums[0]]  # Start the first group

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                group.append(nums[i])
            else:
                groups.append(group)
                group = [nums[i]]  # Start a new group
        
        groups.append(group)  # Add the last group

        # Now format the groups
        res = []
        for g in groups:
            if len(g) == 1:
                res.append(str(g[0]))
            else:
                res.append(f"{g[0]}->{g[-1]}")
        
        return res
