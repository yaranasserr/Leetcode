# Last updated: 9/12/2025, 5:16:15 PM
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(c in "aeiou" for c in s)
        
        