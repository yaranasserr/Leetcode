# Last updated: 4/30/2025, 4:38:03 PM
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([len(str(x))%2 == 0  for x in nums])
        
