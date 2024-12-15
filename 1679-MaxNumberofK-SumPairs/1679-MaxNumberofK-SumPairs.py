class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array
        left, right = 0, len(nums) - 1  # Initialize two pointers
        operations = 0
        
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == k:
                operations += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1
        
        return operations
