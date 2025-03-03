class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller ,bigger , equal= [],[],[]
   
        for  num in nums:
            if num < pivot :
                smaller.append(num)
            elif num > pivot :
                bigger.append(num)
            elif num == pivot :
                equal.append(num)

        res = smaller +equal+bigger
        return res

        

        