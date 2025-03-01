class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1] = nums[i-1]*2 
                nums[i] = 0 

        left = 0
        right = 0

        while right < len(nums):
            if nums[right] != 0:
                # Swap the elements
                nums[left], nums[right] = nums[right], nums[left]
                left += 1  # Move the left pointer to the next position
            right += 1  # Always move the right pointer forward
        
        return nums

                                                                          
        