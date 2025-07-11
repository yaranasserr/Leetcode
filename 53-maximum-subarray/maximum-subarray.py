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

            
        