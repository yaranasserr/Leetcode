from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0 

        rows = len(grid)
        columns = len(grid[0])
        islands = {}  # Dictionary to store islands and their coordinates
        count = 0 

        def dfs(r, c, island_id):
            if r < 0 or c < 0 or r >= rows or c >= columns or grid[r][c] == 0:
                return 

           
            grid[r][c] = 0 

            # Add the coordinate to the current island
            islands[island_id].append((r, c))

            dfs(r + 1, c, island_id)
            dfs(r - 1, c, island_id)
            dfs(r, c + 1, island_id)
            dfs(r, c - 1, island_id)

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:  
                    count += 1
                   
                    islands[count] = []
                
                    dfs(i, j, count)
        if not islands :
            return 0

        max_length = max(len(value) for value in islands.values())
        return max_length
