# Last updated: 12/31/2025, 3:31:47 PM
1
2class Solution:
3    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
4        directions = [[0,1],[0,-1],[1,0],[-1,0]]
5
6        def can_cross(day):
7            grid = [[0]*col for _ in range(row)]
8            for r, c in cells[:day]:
9                grid[r-1][c-1] = 1  
10
11            def dfs(r, c):
12                if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 1:
13                    return False
14                if r == row-1:  # reached bottom
15                    return True
16                grid[r][c] = 1  # mark visited as water to avoid revisiting
17                for dr, dc in directions:
18                    if dfs(r+dr, c+dc):
19                        return True
20                return False
21
22            for j in range(col):
23                if grid[0][j] == 0 and dfs(0, j):
24                    return True
25            return False
26
27        # Binary search over days
28        left, right = 1, len(cells)
29        ans = 0
30        while left <= right:
31            mid = (left + right)//2
32            if can_cross(mid):
33                ans = mid
34                left = mid + 1
35            else:
36                right = mid - 1
37        return ans
38