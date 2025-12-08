# Last updated: 12/8/2025, 5:32:28 PM
1from math import sqrt
2
3
4class Solution:
5    def countTriples(self, n: int) -> int:
6        res = 0
7        # enumerate a and b
8        for a in range(1, n + 1):
9            for b in range(1, n + 1):
10                # determine if it meets the requirements
11                c = int(sqrt(a**2 + b**2 + 1))
12                if c <= n and c**2 == a**2 + b**2:
13                    res += 1
14        return res