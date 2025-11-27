# Last updated: 11/27/2025, 4:40:18 PM
1class Solution:
2    def maxSubarraySum(self, nums: List[int], k: int) -> int:
3        n = len(nums)
4        prefixSum = 0
5        maxSum = -sys.maxsize
6        kSum = [sys.maxsize // 2] * k
7        kSum[k - 1] = 0
8        for i in range(n):
9            prefixSum += nums[i]
10            maxSum = max(maxSum, prefixSum - kSum[i % k])
11            kSum[i % k] = min(kSum[i % k], prefixSum)
12        return maxSum