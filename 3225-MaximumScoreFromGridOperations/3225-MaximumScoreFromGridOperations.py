# Last updated: 4/29/2026, 11:18:21 AM
1class Solution:
2    def maximumScore(self, grid: List[List[int]]) -> int:
3        n = len(grid)
4        m = len(grid[0])
5        if m == 1:
6            return 0
7
8        # prefix sum per column
9        col = [[0]*(n+1) for _ in range(m)]
10        for j in range(m):
11            for i in range(n):
12                col[j][i+1] = col[j][i] + grid[i][j]
13
14        dp = [[0]*(n+1) for _ in range(n+1)]
15        prefMax = [[0]*(n+1) for _ in range(n+1)]
16        suffMax = [[0]*(n+1) for _ in range(n+1)]
17
18        for c in range(1, m):
19
20            newdp = [[0]*(n+1) for _ in range(n+1)]
21
22            for curr in range(n+1):
23                for prev in range(n+1):
24
25                    if curr <= prev:
26                        gain = col[c][prev] - col[c][curr]
27
28                        newdp[curr][prev] = max(
29                            newdp[curr][prev],
30                            suffMax[prev][0] + gain
31                        )
32                    else:
33                        gain = col[c-1][curr] - col[c-1][prev]
34
35                        newdp[curr][prev] = max(
36                            newdp[curr][prev],
37                            suffMax[prev][curr],
38                            prefMax[prev][curr] + gain
39                        )
40
41            # build prefix & suffix
42            for curr in range(n+1):
43
44                prefMax[curr][0] = newdp[curr][0]
45
46                for prev in range(1, n+1):
47                    penalty = 0
48                    if prev > curr:
49                        penalty = col[c][prev] - col[c][curr]
50
51                    prefMax[curr][prev] = max(
52                        prefMax[curr][prev-1],
53                        newdp[curr][prev] - penalty
54                    )
55
56                suffMax[curr][n] = newdp[curr][n]
57
58                for prev in range(n-1, -1, -1):
59                    suffMax[curr][prev] = max(
60                        suffMax[curr][prev+1],
61                        newdp[curr][prev]
62                    )
63
64            dp = newdp
65
66        ans = 0
67        for k in range(n+1):
68            ans = max(ans, dp[0][k], dp[n][k])
69
70        return ans