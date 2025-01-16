class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):
            # Expand the window by moving `right` pointer
            if nums[right] == 0:
                zero_count += 1

            # Shrink the window if zero_count exceeds k
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Update the max length of valid window
            max_length = max(max_length, right - left + 1)
        return max_length

        
        
        