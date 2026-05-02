# Last updated: 5/2/2026, 2:46:35 PM
1class Solution:
2    def rotatedDigits(self, n: int) -> int:
3        return sum(
4            any(c in '2569' for c in s) and not any(c in '347' for c in s)
5            for s in map(str, range(1, n+1))
6        )