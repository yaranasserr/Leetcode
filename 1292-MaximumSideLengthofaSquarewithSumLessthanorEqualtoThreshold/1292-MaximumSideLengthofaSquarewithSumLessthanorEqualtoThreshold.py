# Last updated: 1/19/2026, 1:55:54 PM
1class Solution:
2    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
3        m, n = len(mat), len(mat[0])
4        P = [[0] * (n + 1) for _ in range(m + 1)]
5        for i in range(1, m + 1):
6            for j in range(1, n + 1):
7                P[i][j] = (
8                    P[i - 1][j]
9                    + P[i][j - 1]
10                    - P[i - 1][j - 1]
11                    + mat[i - 1][j - 1]
12                )
13
14        def getRect(x1, y1, x2, y2):
15            return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]
16
17        l, r, ans = 1, min(m, n), 0
18        while l <= r:
19            mid = (l + r) // 2
20            find = any(
21                getRect(i, j, i + mid - 1, j + mid - 1) <= threshold
22                for i in range(1, m - mid + 2)
23                for j in range(1, n - mid + 2)
24            )
25            if find:
26                ans = mid
27                l = mid + 1
28            else:
29                r = mid - 1
30        return ans