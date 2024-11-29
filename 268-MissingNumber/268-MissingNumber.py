class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums) #Length of given array
        summation=n*(n+1)/2  #math formula
        x=summation - sum(nums)
        return int(x)