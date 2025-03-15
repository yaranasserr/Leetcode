class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def check(k, m):
            count = 0  # Number of houses robbed
            i = 0  # Start from the first house

            while i < len(nums):
                if nums[i] <= m:  # Can we rob this house?
                    count += 1
                    if count == k:  # Found at least k houses, return True
                        return True
                    i += 1  # Skip adjacent house

                i += 1  # Move to the next house

            return False  # Not enough houses could be robbed

        l = min(nums)
        r = max(nums)
        while l < r :
            m = (l+r)//2 
            if check(k,m):
                r = m # try smaller
            else:
                l= m+1
        return l 

        





        