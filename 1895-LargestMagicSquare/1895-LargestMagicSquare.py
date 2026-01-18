# Last updated: 1/18/2026, 2:28:54 PM
1class Solution:
2    def largestMagicSquare(self, grid: List[List[int]]) -> int:
3        m, n = len(grid), len(grid[0])
4        res = 1
5
6        def isValid(i, j, k):
7            s = None
8            for x in range(i, i + k):
9                row = sum(grid[x][j:j + k])
10                if s is None: s = row
11                elif s != row: return False
12
13            for y in range(j, j + k):
14                if sum(grid[x][y] for x in range(i, i + k)) != s:
15                    return False
16
17            if sum(grid[i + d][j + d] for d in range(k)) != s:
18                return False
19
20            if sum(grid[i + d][j + k - 1 - d] for d in range(k)) != s:
21                return False
22
23            return True
24
25        for k in range(2, min(m, n) + 1):
26            for i in range(m - k + 1):
27                for j in range(n - k + 1):
28                    if isValid(i, j, k):
29                        res = k
30        return res