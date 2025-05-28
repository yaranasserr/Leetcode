# Last updated: 5/28/2025, 10:10:04 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Helper function to run DFS + memo on a slice
        def rob_linear(houses: List[int]) -> int:
            n = len(houses)
            cache = [-1] * n

            def dfs(i):
                if i >= n:
                    return 0
                if cache[i] != -1:
                    return cache[i]
                cache[i] = max(houses[i] + dfs(i + 2), dfs(i + 1))
                return cache[i]

            return dfs(0)

        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))