# Last updated: 5/15/2025, 5:58:48 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        res = [1] * n

        left[0] = right[n-1] = 1

        # left 
        for i in range(1,n):
            left[i] = left[i-1] *nums[i-1]

        # right 
        for i in range(n-2,-1,-1):
            right[i] = right [i+1] *nums[i+1]



        for i in range(n):
            res[i] = left[i]*right[i]

        return res 

      