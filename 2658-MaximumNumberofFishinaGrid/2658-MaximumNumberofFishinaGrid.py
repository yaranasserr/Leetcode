class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        maximum = 0 

        def dfs(r,c):
           
            if r < 0 or c < 0 or r >= rows or c >= columns or grid[r][c] == 0 :
                return 0

            # mark fish as visited 
            fish_count = grid[r][c]
            grid[r][c] = 0 
            return (fish_count + dfs(r,c+1) + dfs(r,c-1) +dfs(r+1,c)+ dfs(r-1,c))

        

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] > 0:
                    amount = dfs(i,j)
                    
                    maximum = max(maximum,amount)

        return maximum
        