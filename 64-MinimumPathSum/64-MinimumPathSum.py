# Last updated: 7/23/2025, 6:21:03 PM
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        memo = {}
        def find(r,c):
            if r>= m or c >= n :
                return float("inf")


            if r == m-1 and c== n-1 :
                return grid[r][c]


            if (r,c) in memo :
                return memo[(r,c)]


            memo[(r,c)] = grid[r][c] + min(find(r+1,c),find(r,c+1))

            return memo[(r,c)]


        return find(0,0)
        



        