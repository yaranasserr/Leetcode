class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [num for num , cnt in Counter(nums).items() if cnt ==2]
        