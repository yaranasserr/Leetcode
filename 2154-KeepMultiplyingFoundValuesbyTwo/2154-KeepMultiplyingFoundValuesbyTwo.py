# Last updated: 11/19/2025, 10:42:36 AM
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:

        while original in nums :
            original *=2 
        return original
        