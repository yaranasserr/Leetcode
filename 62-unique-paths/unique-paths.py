class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp ={}

        def dfs(r,c):
            if r == m-1 and c == n-1 :
                return  1
            if r > m or c > n :
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            dp[(r, c)] =dfs(r+1,c) + dfs(r,c+1)


            return dp[(r, c)]


        return dfs(0,0)



























        # from functools import lru_cache
        # # least recently used

        # @lru_cache(None)
        # def find(r, c):
        #     # Base case: if we reach the bottom-right corner, there's 1 unique path
        #     if r == m - 1 and c == n - 1:
        #         return 1

        #     # If out of bounds, return 0
        #     if r >= m or c >= n:
        #         return 0

        #     # Move down and right
        #     return find(r + 1, c) + find(r, c + 1)

        # # Start from the top-left corner
        # return find(0, 0)
