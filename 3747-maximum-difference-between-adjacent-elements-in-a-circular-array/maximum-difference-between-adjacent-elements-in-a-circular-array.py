class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        diff = []

        for i in range(1,n):
            diff.append(abs(nums[i]-nums[i-1]))

        diff.append(abs(nums[0]-nums[n-1]))
        return max(diff)
        