class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0  # unique 
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                # not duplicates 
                i +=1 
            nums[i] = nums[j] #This places the new unique value right after the last unique value we kept.

        return i+1 
        