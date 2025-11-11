from typing import List
from collections import defaultdict

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = defaultdict(int)
        
        for s in strs:
            zeros = s.count("0")
            ones = s.count("1")
            
            # Use new loop vars to avoid overwriting m and n
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[(i, j)] = max(1 + dp[(i - zeros, j - ones)], dp[(i, j)])
        
        return dp[(m, n)]
