from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        maximum = 0

        def dfs(r, c):
            # Base case: Out of bounds or water cell
            if r < 0 or c < 0 or r >= rows or c >= columns or grid[r][c] == 0:
                return 0

            # Mark the cell as visited
            grid[r][c] = 0

            # Recursively calculate the area of the island
            return 1 + dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c)

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    # Calculate the area of the current island
                    area = dfs(i, j)
                    # Update the maximum area
                    maximum = max(area, maximum)

        return maximum
