# Last updated: 4/29/2025, 4:05:23 PM
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        count = 0 
        n = len(nums)
        max_count = 0 
        # sliding window 
        # as longs as count(max) < k , expand 
        l = 0 
        for r in range(n):
            if nums[r] == maximum :
                max_count +=1
            while max_count >= k :
                count += (n-r)

                if nums[l] == maximum :
                    max_count -=1

                l+=1
        return count 




        #     while nums[l:r+1].count(maximum) >=k  :
        #         count +=(r-l+1)
        #     l+=1
        # return count 


        