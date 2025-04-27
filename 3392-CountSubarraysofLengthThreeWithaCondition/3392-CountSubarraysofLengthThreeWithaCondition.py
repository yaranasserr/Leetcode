# Last updated: 4/27/2025, 5:21:28 PM
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
      
        count = 0 
        n =len(nums)
        l = 0 
        for r in range(2,n):
            sub = nums[l:r+1]
            l+=1
            if sub[0] + sub [2] == sub[1] /2 :
                count +=1 
        return count 

        