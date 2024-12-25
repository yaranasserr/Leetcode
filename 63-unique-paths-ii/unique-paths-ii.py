class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # obstacle -> 1
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        from functools import lru_cache

        @lru_cache(None)

        def find(r,c):
            if not obstacleGrid:
                return 
            if obstacleGrid[0][0] == 1:
                return 0 
                
            if r == m-1 and c == n -1 :
                return 1

            if r >= m or c >= n or obstacleGrid[r][c] == 1 or obstacleGrid[m-1][n-1] == 1  :
                return 0
            
            return find(r + 1, c) + find(r, c + 1)

        return find(0,0)
        