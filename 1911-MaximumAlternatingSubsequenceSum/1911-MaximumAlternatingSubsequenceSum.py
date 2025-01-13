
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        sumEven , sumOdd = 0,0 
        for i in range(len(nums)-1,-1,-1):
            tmpEven = max(sumEven ,sumOdd+nums[i])
            tmpOdd = max(sumOdd , sumEven - nums[i])

            sumEven , sumOdd = tmpEven , tmpOdd
        return sumEven

