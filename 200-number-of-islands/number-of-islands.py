class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0 

        rows , cols = len(grid), len(grid[0])
        island_count =0
            

        def dfs(r, c):
            # Check bounds and whether the cell is land
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return

            # Mark the cell as visited by changing it to water ('0')
            grid[r][c] = "0"

            # Visit all 4 adjacent cells (up, down, left, right)
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    island_count += 1
                    dfs(i, j)  # Start DFS to mark the entire island as visited

        return island_count
