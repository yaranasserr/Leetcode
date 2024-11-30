class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_subarray = nums[0]
        current_sum = 0
        
        for number in nums:
            if current_sum < 0:
                current_sum = 0
                
            current_sum = current_sum + number

            if current_sum > max_subarray:
                max_subarray = current_sum
                
        return max_subarray
        