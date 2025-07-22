# Last updated: 7/22/2025, 2:33:15 PM
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0 
        sub = []
        maximum = 0 
        curr_sum = 0 
        for r in range(len(nums)):
            while nums[r] in sub :
                curr_sum -= sub[0]
                sub.remove(nums[l])
                l+=1
            sub.append(nums[r])
            curr_sum += nums[r]
       
            maximum = max(maximum,curr_sum)
           

        return maximum


        