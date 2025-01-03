from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize variables to track the maximum and minimum products
        # and the result.
        max_product = nums[0]
        min_product = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            # If the current number is negative, swap max and min products
            if nums[i] < 0:
                max_product, min_product = min_product, max_product
            
            # Update max_product and min_product considering the current number
            max_product = max(nums[i], nums[i] * max_product)
            min_product = min(nums[i], nums[i] * min_product)
            
            # Update the result with the current max_product
            res = max(res, max_product)
        
        return res

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:

        # dp = [1] * len(nums)
        # res = max(nums)

        # dp[0] = nums[0]

        # for i in range(1,len(nums)):
        #     dp[i] = nums[i] * dp[i-1]


        # return max(res,max(dp))



        