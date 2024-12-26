from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        #dynamic programming solution  bottom up 

        res =[[float("inf")] * (cols+1) for r in range(rows+1)]

        res[rows-1][cols]=0
        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                res[r][c] = grid[r][c] + min(res[r+1][c],res[r][c+1])
        return res[0][0]

        #recusrion
        # memo = {}

        # def find(r, c):
        #     # If out of bounds, return infinity (invalid path)
        #     if r >= rows or c >= cols:
        #         return float('inf')
            
        #     # If at the bottom-right corner, return its value
        #     if r == rows - 1 and c == cols - 1:
        #         return grid[r][c]

        #     # If already computed, return the stored value
        #     if (r, c) in memo:
        #         return memo[(r, c)]

        #     # Compute the minimum path sum recursively
        #     memo[(r, c)] = grid[r][c] + min(find(r + 1, c), find(r, c + 1))
        #     return memo[(r, c)]

        # return find(0, 0)
