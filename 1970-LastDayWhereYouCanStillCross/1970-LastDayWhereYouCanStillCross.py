# Last updated: 12/31/2025, 3:31:13 PM
1from typing import List
2
3class Solution:
4    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
5        directions = [[0,1],[0,-1],[1,0],[-1,0]]
6
7        def can_cross(day: int) -> bool:
8            grid = [[0]*col for _ in range(row)]
9            for r, c in cells[:day]:
10                grid[r-1][c-1] = 1  
11
12            def dfs(r, c):
13                if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 1:
14                    return False
15                if r == row-1:  # reached bottom
16                    return True
17                grid[r][c] = 1  # mark visited as water to avoid revisiting
18                for dr, dc in directions:
19                    if dfs(r+dr, c+dc):
20                        return True
21                return False
22
23            for j in range(col):
24                if grid[0][j] == 0 and dfs(0, j):
25                    return True
26            return False
27
28        # Binary search over days
29        left, right = 1, len(cells)
30        ans = 0
31        while left <= right:
32            mid = (left + right)//2
33            if can_cross(mid):
34                ans = mid
35                left = mid + 1
36            else:
37                right = mid - 1
38        return ans
39