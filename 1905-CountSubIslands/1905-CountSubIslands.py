from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        if not grid1 or not grid2:
            return 0  # Return 0 for invalid input
        
        rows, columns = len(grid1), len(grid1[0])

        def dfs(r, c):
            # If out of bounds or the cell is water in either grid
            if r < 0 or c < 0 or r >= rows or c >= columns or grid2[r][c] == 0:
                return True

            # If the cell in grid2 is part of an island but grid1 does not have it
            if grid1[r][c] == 0:
                return False

            # Mark the cell in grid2 as visited
            grid2[r][c] = 0

            # Recursively check all four directions and combine results
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)

            return up and down and left and right

        count = 0
        for i in range(rows):
            for j in range(columns):
                if grid2[i][j] == 1:  # Found an unvisited cell in grid2
                    if dfs(i, j):    # Check if it's a sub-island
                        count += 1

        return count
