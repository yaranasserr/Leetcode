class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # duplicates cancel eachother
        res =0 
        for num in nums:
            res = res^ num 

        return res