# Last updated: 1/2/2026, 1:30:15 PM
1class Solution:
2    def repeatedNTimes(self, nums: List[int]) -> int:
3        return next(k for k,v in Counter(nums).items() if v == (len(nums)//2))
4        