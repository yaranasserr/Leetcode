# Last updated: 7/10/2025, 6:09:28 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1

        while l <= r :
            mid = (l+r)//2

            if nums[mid] < target : 
                l = mid+1
            elif nums[mid] > target :
                r = mid -1 
            elif nums[mid] == target :
                return mid 

        return l 

       

        