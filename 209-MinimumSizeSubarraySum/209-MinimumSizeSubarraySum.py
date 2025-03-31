# Last updated: 3/31/2025, 8:09:19 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window
        length = float("inf")
        l=0 
        summ= 0 

        

        for r in range(len(nums)):
        
            summ += nums[r]

            while summ >= target :
                length = min(length,r-l+1)
                summ -= nums[l]
                l+=1

        return length if length != float("inf") else 0

    # O(N)

        

        