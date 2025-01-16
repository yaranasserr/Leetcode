class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):
            # Include the current element in the window
            if nums[right] == 0:
                zero_count += 1

            # If the window has more than one zero, shrink it from the left
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Calculate the size of the current window
            max_length = max(max_length, right - left + 1)

        # Subtract 1 to account for the one element that needs to be deleted
        return max_length - 1
    