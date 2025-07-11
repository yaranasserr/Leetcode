# Last updated: 7/11/2025, 7:21:41 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = min(nums)
        cur = 0 
        for n in nums :
            cur+= n 
            maximum = max(cur,maximum)
            if cur < 0 :
                cur = 0 

        return maximum

            
        