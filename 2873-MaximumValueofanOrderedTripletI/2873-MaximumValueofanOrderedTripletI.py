# Last updated: 4/2/2025, 4:18:38 PM
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        N = len(nums)
        left = nums[0]
        for j in range(1,N):
            if nums[j]>left :
                left = nums[j]
                continue

            for k in range(j+1,N):
                res=max(res,(left-nums[j])*nums[k])

        return res
        