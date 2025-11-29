# Last updated: 11/29/2025, 7:42:15 PM
1class Solution:
2    def minOperations(self, nums: List[int], k: int) -> int:
3        return sum(nums) % k