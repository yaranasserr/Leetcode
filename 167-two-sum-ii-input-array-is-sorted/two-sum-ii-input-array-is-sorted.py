class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diffs = {}

        for i , num in enumerate(numbers):
            difference = target - num
            if difference in diffs :
                return[diffs[difference]+1,i+1]
            diffs[num] = i
        return []

        