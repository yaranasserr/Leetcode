# Last updated: 12/28/2025, 1:58:43 PM
1class Solution:
2    def countNegatives(self, grid: List[List[int]]) -> int:
3        count = 0 
4        for r in range(len(grid)):
5            for c in range(len(grid[0])):
6                if grid[r][c] < 0 :
7                    count +=1
8
9        return count
10        