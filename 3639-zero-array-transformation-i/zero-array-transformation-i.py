class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)

        for l, r in queries:
            diff[l] += 1
            if r + 1 < len(diff):
                diff[r + 1] -= 1

        # Prefix sum on the diff array to get count array
        prefix = [0] * n
        prefix[0] = diff[0]
        for i in range(1, n):
            prefix[i] = diff[i] + prefix[i - 1]

        # Compare available operations to nums[i]
        for i in range(n):
            if prefix[i] < nums[i]:
                return False

        return True