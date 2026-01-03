# Last updated: 1/3/2026, 8:52:12 PM
1class Solution:
2    def numOfWays(self, n: int) -> int:
3        MOD = 1000000007
4        x, y = 6, 6
5        
6        for i in range(2, n + 1):
7            new_x = (3 * x + 2 * y) % MOD
8            new_y = (2 * x + 2 * y) % MOD
9            x, y = new_x, new_y
10        
11        return (x + y) % MOD