class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # max absolute sum will be either the max sum or the min sum
        #kadane twice, once calculating the max sum and once calculating the min sum.
        maxsum = nums[0]
        curmax=0

        minsum=nums[0]
        curmin = 0

        for n in nums :
            curmax = max(curmax,0) # reset on negatives
            curmax+= n
            maxsum=max(maxsum,curmax)

            curmin = min(curmin,0) 
            curmin+= n 
            minsum=min(curmin,minsum)

        return max(maxsum,abs(minsum))



            


        