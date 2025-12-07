# Last updated: 12/7/2025, 6:43:21 PM
1class Solution:
2    def countOdds(self, low: int, high: int) -> int:
3        return (high + 1) // 2 - (low // 2)