# Last updated: 3/9/2026, 3:24:51 PM
1class Solution:
2    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
3        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
4        mod = int(1e9 + 7)
5        for i in range(min(zero, limit) + 1):
6            dp[i][0][0] = 1
7        for j in range(min(one, limit) + 1):
8            dp[0][j][1] = 1
9        for i in range(1, zero + 1):
10            for j in range(1, one + 1):
11                if i > limit:
12                    dp[i][j][0] = (
13                        dp[i - 1][j][0]
14                        + dp[i - 1][j][1]
15                        - dp[i - limit - 1][j][1]
16                    )
17                else:
18                    dp[i][j][0] = dp[i - 1][j][0] + dp[i - 1][j][1]
19                dp[i][j][0] = (dp[i][j][0] % mod + mod) % mod
20                if j > limit:
21                    dp[i][j][1] = (
22                        dp[i][j - 1][1]
23                        + dp[i][j - 1][0]
24                        - dp[i][j - limit - 1][0]
25                    )
26                else:
27                    dp[i][j][1] = dp[i][j - 1][1] + dp[i][j - 1][0]
28                dp[i][j][1] = (dp[i][j][1] % mod + mod) % mod
29        return (dp[zero][one][0] + dp[zero][one][1]) % mod