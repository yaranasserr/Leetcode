# Last updated: 10/31/2025, 11:23:55 AM
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [num for num , cnt in Counter(nums).items() if cnt ==2]
        