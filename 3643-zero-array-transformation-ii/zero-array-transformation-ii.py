class Solution(object):
    def canFormZeroArray(self, nums, queries, k):
        n = len(nums)
        diff = [0] * (n + 1)

        # Apply the first k queries to the difference array
        for i in range(k):
            l, r, val = queries[i]
            diff[l] += val
            if r + 1 < len(diff):
                diff[r + 1] -= val

        # Reconstruct the array using prefix sum
        sum_ = 0
        for i in range(n):
            sum_ += diff[i]
            if sum_ < nums[i]:
                return False
        return True

    def minZeroArray(self, nums, queries):
        n = len(nums)
        l, r = 0, len(queries)
        res = -1

        # Binary search to find the minimum number of queries needed
        while l <= r:
            mid = (l + r) // 2
            if self.canFormZeroArray(nums, queries, mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res
