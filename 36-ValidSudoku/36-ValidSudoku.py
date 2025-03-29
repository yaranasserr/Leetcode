# Last updated: 3/29/2025, 11:57:05 PM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0 , len(nums)-1
        res = nums[0]

        while l<=r :
            # array is sorted 
            if nums[l]<nums[r]:
                res = min(res,nums[l])
                break 

            # mid in left portion -> search in the right
            mid = (l+r)//2
            res = min(res,nums[mid]) 
            if nums[mid]>= nums[l]:
                l= mid+1 
            else:
                r = mid -1 

        return res



        