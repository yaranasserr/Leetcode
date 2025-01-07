class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
            
        while left < right:
            mid = (left + right) // 2
                
                # Compare mid with its right neighbor
            if nums[mid] > nums[mid + 1]:
                    # Peak is in the left half (including mid)
                    right = mid
            else:
                    # Peak is in the right half
                left = mid + 1
            
            # left and right will converge to the peak
        return left