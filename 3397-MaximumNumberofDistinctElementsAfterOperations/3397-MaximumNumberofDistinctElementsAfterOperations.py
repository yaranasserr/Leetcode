# Last updated: 10/18/2025, 10:06:17 PM
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()

        cnt = 0
        prev = -math.inf

        for num in nums:
            curr = min(max(num - k, prev + 1), num + k)
            if curr > prev:
                cnt += 1
                prev = curr

        return cnt