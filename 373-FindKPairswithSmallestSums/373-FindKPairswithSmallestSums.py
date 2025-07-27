# Last updated: 7/27/2025, 4:48:27 PM
class Solution:
    def trailingZeroes(self, n):
        x   = 5
        res = 0
        while x <= n:
            res += n//x
            x   *= 5
        return res