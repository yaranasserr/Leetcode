# Last updated: 9/8/2025, 11:17:17 AM
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def no_zero(x: int) -> bool:
            return '0' not in str(x)
        
        for a in range(1, n):
            b = n - a
            if no_zero(a) and no_zero(b):
                return [a, b]
