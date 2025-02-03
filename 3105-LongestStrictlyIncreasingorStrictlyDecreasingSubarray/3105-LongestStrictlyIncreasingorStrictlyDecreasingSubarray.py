class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = maximum = 1
        
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                inc+=1
                dec = 1
                
            elif nums[i] < nums[i-1]:
                dec+=1
                inc = 1
            else :
                inc = dec = 1

                

            maximum=max(inc,dec,maximum)

        return maximum

            

        