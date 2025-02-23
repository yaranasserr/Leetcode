class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_length = 0 
        start = first_neg = -1
        neg = 0 
        for i , num in enumerate(nums):
            if num == 0 :
                start , first_neg , neg = i, -1 , 0 
            else:
                if num < 0:
                    neg += 1
                    if first_neg == -1:
                        first_neg = i
                max_length = max(max_length, i - start if neg % 2 == 0 else i - first_neg)

        return max_length




            

            