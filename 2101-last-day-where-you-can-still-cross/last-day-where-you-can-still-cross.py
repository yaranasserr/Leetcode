from typing import List

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def can_cross(day: int) -> bool:
            grid = [[0]*col for _ in range(row)]
            for r, c in cells[:day]:
                grid[r-1][c-1] = 1  

            def dfs(r, c):
                if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 1:
                    return False
                if r == row-1:  # reached bottom
                    return True
                grid[r][c] = 1  # mark visited as water to avoid revisiting
                for dr, dc in directions:
                    if dfs(r+dr, c+dc):
                        return True
                return False

            for j in range(col):
                if grid[0][j] == 0 and dfs(0, j):
                    return True
            return False

        # Binary search over days
        left, right = 1, len(cells)
        ans = 0
        while left <= right:
            mid = (left + right)//2
            if can_cross(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
