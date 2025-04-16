# Last updated: 4/16/2025, 4:42:16 PM
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # sliding window 

        n = len(nums)
        left = 0
        pairs = 0
        freq = defaultdict(int)
        res = 0

        for right in range(n):
            pairs += freq[nums[right]]
            freq[nums[right]] += 1

            while pairs >= k:
                res += n - right  # all subarrays [left, right] to [left, n-1] are good
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left += 1

        return res