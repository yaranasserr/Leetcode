# Last updated: 10/29/2025, 11:39:24 AM
class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        while x < n:
            x = x * 2 + 1
        return x