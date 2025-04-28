# Last updated: 4/28/2025, 4:51:49 PM
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0 
        l = 0 
        cur_sum = 0 
        n = len(nums)
        for r in range(n):
            cur_sum += nums[r]

            while l <= r and cur_sum * (r - l + 1) >= k:
                cur_sum -= nums[l]
                l += 1

            count += (r - l + 1)

        return count
