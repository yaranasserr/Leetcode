# Last updated: 6/16/2025, 12:29:08 PM
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1 
        premin = nums[0]

        for i in range(1,len(nums)):
            if nums[i] > premin:
                ans = max(ans,nums[i]-premin)

            else:
                premin = nums[i]

        return ans
        

        