# Last updated: 3/31/2025, 5:50:09 PM
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
                print(length)
                summ -= nums[l]
                l+=1

        return length if length != float("inf") else 0

        

        