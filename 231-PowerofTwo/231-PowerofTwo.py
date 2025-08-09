# Last updated: 8/9/2025, 1:01:59 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and n & (n-1) == 0