# Last updated: 10/25/2025, 12:55:24 PM
class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        monday = 1
        
        while n > 0:
            for day in range(min(n, 7)):
                ans += monday + day
            
            n -= 7
            monday += 1

        return ans