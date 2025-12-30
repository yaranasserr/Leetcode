# Last updated: 12/30/2025, 10:47:10 PM
1class Solution:
2    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
3        ans = 0
4        m = len(grid)
5        n = len(grid[0])
6        for row in range(m - 2):
7            for col in range(n - 2):
8                if self._isMagicSquare(grid, row, col):
9                    ans += 1
10        return ans
11
12    def _isMagicSquare(self, grid, row, col):
13        seen = [False] * 10
14        for i in range(3):
15            for j in range(3):
16                num = grid[row + i][col + j]
17                if num < 1 or num > 9:
18                    return False
19                if seen[num]:
20                    return False
21                seen[num] = True
22
23        # Check if diagonal sums are the same
24        diagonal1 = (
25            grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
26        )
27        diagonal2 = (
28            grid[row + 2][col] + grid[row + 1][col + 1] + grid[row][col + 2]
29        )
30
31        if diagonal1 != diagonal2:
32            return False
33
34        # Check if all row sums are the same as the diagonal sums
35        row1 = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]
36        row2 = (
37            grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2]
38        )
39        row3 = (
40            grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]
41        )
42
43        if not (row1 == diagonal1 and row2 == diagonal1 and row3 == diagonal1):
44            return False
45
46        # Check if all column sums are the same as the diagonal sums
47        col1 = grid[row][col] + grid[row + 1][col] + grid[row + 2][col]
48        col2 = (
49            grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]
50        )
51        col3 = (
52            grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]
53        )
54
55        if not (col1 == diagonal1 and col2 == diagonal1 and col3 == diagonal1):
56            return False
57
58        return True