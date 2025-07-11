# Last updated: 7/11/2025, 7:28:44 PM
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)

        def maxsubarry(nums):
            maximum = float("-inf")
            cur = 0 
            for n in nums:
                cur += n 
                maximum = max(cur, maximum)
                if cur < 0:
                    cur = 0 
            return maximum

        def minsubarry(nums):
            minimum = float("inf")
            cur = 0 
            for n in nums:
                cur += n 
                minimum = min(cur, minimum)
                if cur > 0:
                    cur = 0 
            return minimum

        max_kadane = maxsubarry(nums)
        min_kadane = minsubarry(nums)

        # Edge case: all numbers are negative
        if max_kadane < 0:
            return max_kadane
        
        return max(max_kadane, total - min_kadane)
