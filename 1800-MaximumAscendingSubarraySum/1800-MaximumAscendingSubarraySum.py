class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
       
        n=len(nums)
        cur = nums[0]
        res= cur


        for i  in range(1,n):
            if nums[i-1] < nums[i]:
                cur += nums[i]
            else :
                cur = nums[i]

            res = max(res,cur)
               


        return res

               

        