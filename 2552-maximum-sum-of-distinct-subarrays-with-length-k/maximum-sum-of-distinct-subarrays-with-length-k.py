from collections import Counter
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = Counter()
        max_sum = 0
        window_sum = 0
        l = 0

        for r in range(len(nums)):
            # Add new element to the window
            freq[nums[r]] += 1
            window_sum += nums[r]

            # Ensure window size does not exceed k
            if r - l + 1 > k:
                freq[nums[l]] -= 1
                window_sum -= nums[l]
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1

            # Check if window is of size k and has all unique elements
            if r - l + 1 == k and len(freq) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum
