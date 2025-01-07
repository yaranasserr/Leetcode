from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # DP approach with O(n^2) complexity
        # dp dictionary: key = index, value = [length of LIS ending at index, count of such LIS]
        dp = {} 
        lenLIS, res = 0, 0  # Overall length of LIS, total count of LIS

        # Iterate backwards through the list to calculate LIS for each starting index
        for i in range(len(nums) - 1, -1, -1):
            maxLen, maxcnt = 1, 1  # Initialize length and count for the current index

            # Check all subsequent elements to find valid LIS extensions
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:  # Valid extension of LIS
                    length, count = dp[j]
                    if length + 1 > maxLen:
                        # Found a longer LIS
                        maxLen, maxcnt = length + 1, count
                    elif length + 1 == maxLen:
                        # Found another LIS of the same length
                        maxcnt += count

            # Update overall LIS length and count
            if maxLen > lenLIS:
                lenLIS, res = maxLen, maxcnt
            elif lenLIS == maxLen:
                res += maxcnt

            # Store the LIS details for the current index
            dp[i] = [maxLen, maxcnt]

        return res
