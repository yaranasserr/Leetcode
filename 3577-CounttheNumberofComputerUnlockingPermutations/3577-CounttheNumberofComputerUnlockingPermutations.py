# Last updated: 12/10/2025, 2:16:00 PM
1class Solution:
2    def countPermutations(self, complexity: List[int]) -> int:
3        n = len(complexity)
4        for i in range(1, n):
5            if complexity[i] <= complexity[0]:
6                return 0
7
8        ans, mod = 1, 10**9 + 7
9        for i in range(2, n):
10            ans = ans * i % mod
11        return ans