from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        def getxandf(nums):
            freq = {}
            for i in nums:
                freq[i] = 1 + freq.get(i, 0)
            f = max(freq.values())
            x = max(freq, key=freq.get)  # Get the dominant element
            return x, f  # Return single dominant element, not a list
        
        x, f = getxandf(nums)  # Get dominant element and its frequency
        left_count = 0  # Count occurrences of x in left subarray
        n = len(nums)
        
        for i in range(n - 1):  # Ensure a valid split (0 ≤ i < n-1)
            if nums[i] == x:
                left_count += 1  # Increment count of x in left subarray
            
            right_count = f - left_count  # Remaining occurrences of x in right subarray
            
            # Check dominance condition
            if left_count * 2 > (i + 1) and right_count * 2 > (n - (i + 1)):
                return i  # Return the minimum valid split index
        
        return -1  # No valid split found
