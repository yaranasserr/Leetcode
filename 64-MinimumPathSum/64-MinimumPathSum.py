# Last updated: 7/29/2025, 9:40:54 PM
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # top down 
        m = len(grid)
        n = len(grid[0])
        dp ={}

        def dfs(r,c):
            if r <0 or c < 0 or r>= m or c>=n :
                return float("inf")

            if r == m-1 and c == n-1:
                return grid[r][c]

            if (r,c) in dp :
                return dp[(r,c)]

            dp[(r,c)] = grid[r][c]+min(dfs(r+1,c),dfs(r,c+1))

            return dp[(r,c)]

        return dfs(0,0)
       
        # Time Complexity: O(m * n)


# Without memoization, the recursion would branch into two calls at each step (down and right), leading to an exponential number of calls: O(2^(m+n)).
        