from typing import List
from collections import defaultdict

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        def out_of_bounds(r, c):
            return r < 0 or c < 0 or r >= N or c >= N  # Fixed boundary condition

        def dfs(r, c, label):
            if out_of_bounds(r, c) or grid[r][c] == 0 or grid[r][c] == label:
                return 0 
            grid[r][c] = label
            size = 1
            neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            for nr, nc in neighbors:
                size += dfs(nr, nc, label)
            return size

        # Compute island areas
        size = defaultdict(int)  # island label -> area
        label = 2
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    size[label] = dfs(r, c, label)
                    label += 1

        def connect(r, c):
            neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            visit = set()
            res = 1
            for nr, nc in neighbors:
                if not out_of_bounds(nr, nc) and grid[nr][nc] not in visit:
                    res += size[grid[nr][nc]]
                    visit.add(grid[nr][nc])
            return res

        # Try flipping water
        res = max(size.values(), default=0)  # Fixed incorrect function call
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    res = max(res, connect(r, c))

        return res
