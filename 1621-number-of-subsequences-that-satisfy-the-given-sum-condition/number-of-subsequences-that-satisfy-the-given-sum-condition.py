class Solution:
    def numSubseq(self, nums, target):
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)
        res = 0 

        r = n -1 

        for i , l in enumerate(nums):
            while (l +nums[r]) > target and i <= r :
                r -=1

            if i <= r :
                res  += (2**(r-i))
                res %= mod 

        return res 

