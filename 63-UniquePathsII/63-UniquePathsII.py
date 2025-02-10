class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = {}
        m= len(obstacleGrid)
        n=len(obstacleGrid[0])

        def dfs(r,c):
            if not obstacleGrid:
                return 
            if obstacleGrid[0][0] == 1:
                return 0 
            if r== m-1 and c == n-1:
                return 1 
            # base cases 
            if r >= m or c >= n or obstacleGrid[r][c] == 1 or obstacleGrid[m-1][n-1] == 1:
                return 0 
            # memo
            if (r,c) in dp :
                return dp[(r,c)]
            
            dp[(r,c)] = dfs(r+1,c) +dfs(r,c+1)
            return dp[(r,c)]

        return dfs(0,0)
