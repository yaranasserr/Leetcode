class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
            
                
        for i in range(0,len(nums)):
            if (i<len(nums)-1):
                if(nums[i]!=nums[i+1] and nums[i]!= nums[i-1]):
                        return nums[i]
                
                 
                elif(nums[len(nums)-1]!= nums[len(nums)-2]):
                    return nums[len(nums)-1]
                
                
                
                
                
                
           
            
            
            
        