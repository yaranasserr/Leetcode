# Last updated: 10/6/2025, 2:17:31 PM
class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        res = 0 
        for n in range(len(nums)):
            if n %2 == 0:
                res += nums[n]
            else:
                res -= nums[n]

        return res 
        