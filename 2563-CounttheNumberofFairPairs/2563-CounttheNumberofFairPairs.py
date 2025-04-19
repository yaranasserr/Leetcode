# Last updated: 4/19/2025, 4:23:00 PM
from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def lower_bound(nums, target, start):
            l = start
            r = len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l

        def upper_bound(nums, target, start):
            l = start
            r = len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid
            return l

        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n):
            left = lower - nums[i]
            right = upper - nums[i]
            l = lower_bound(nums, left, i + 1)
            r = upper_bound(nums, right, i + 1)
            count += r - l

        return count
