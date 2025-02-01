class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # parity even or odd 
        n= len(nums)
        if n ==1:
            return True

        for i in range(1,n):
            if nums[i-1] % 2 == nums[i] % 2 :

                return False
           
          
        return True 

        