# Last updated: 12/20/2025, 11:35:06 AM
1class Solution:
2    def minDeletionSize(self, strs: List[str]) -> int:
3        res = 0
4
5        for col in range(len(strs[0])):
6            for row in range(1, len(strs)):
7                if strs[row][col] < strs[row - 1][col]:
8                    res += 1
9                    break
10
11        return res
12