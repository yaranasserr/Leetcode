# Last updated: 5/27/2025, 11:36:31 AM
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
    
        return sum([x if x%m != 0 else 0 for x in range(1,n+1)
])- sum([x if x%m == 0 else 0 for x in range(1,n+1)])