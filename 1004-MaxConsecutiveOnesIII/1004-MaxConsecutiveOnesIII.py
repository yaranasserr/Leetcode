# Last updated: 7/29/2025, 10:48:54 PM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0 
        z_c = 0 
        maxlength = 0 
        for r in range(len(nums)):
            if nums[r] == 0 :
                z_c+=1

            while z_c >k :
                if nums[l] == 0 :
                    z_c -=1

                l+=1

            maxlength = max(maxlength,r-l+1)


        return maxlength

        