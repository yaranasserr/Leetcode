# Last updated: 8/7/2026, 8:06:41 PM
1class Solution:
2    def smallestNumber(self, n: int, t: int) -> int:
3        def check(num: int) -> bool:
4            product = 1
5            while num > 0:
6                product *= num % 10
7                num //= 10
8                if product == 0:
9                    break
10            return product % t == 0
11
12        while not check(n):
13            n += 1
14        return n
15        