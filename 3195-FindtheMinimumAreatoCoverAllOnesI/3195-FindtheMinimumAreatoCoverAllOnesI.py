# Last updated: 8/22/2025, 3:12:01 PM
from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        min_r, max_r = rows, -1
        min_c, max_c = cols, -1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    min_r = min(min_r, r)
                    max_r = max(max_r, r)
                    min_c = min(min_c, c)
                    max_c = max(max_c, c)

        if max_r == -1:  # no 1's in the grid
            return 0

        return (max_r - min_r + 1) * (max_c - min_c + 1)
