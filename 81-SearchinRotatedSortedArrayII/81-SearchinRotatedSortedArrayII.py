// Last updated: 3/22/2025, 1:16:26 PM
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums= list(set(nums))
      
        
        l,r = 0 , len(nums)-1

        while l <= r :
            m = (l+r)//2
            if nums[m] == target :
                return True 

            if nums[l] <= nums[m]:
                if nums[l]<= target <= nums[m] :
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m]>= target >= nums[r]:
                    l = m +1
                else:
                    r = m-1 
                    


        return False 
        