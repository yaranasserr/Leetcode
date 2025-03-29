class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) -1 

        while l<= r :
                
            mid=(l+r)//2
            if nums[mid] == target :
                return mid 
            # determine which half is sorted 
            # left half is sorted
            if nums[l] <= nums[mid]:
                # target in left half 
                if nums[l]<= target <= nums[mid]:
                    r = mid -1 
                else:
                    l = mid+1  # target in right half 

            # right half is sorted :

            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid+1
                else:
                    r = mid -1 
        return -1 






            # if target < mid -> search in right 
            # if nums[mid] >target  and nums[l] >= nums[r]:
            #     l = mid +1
            # elif nums[mid] < target and nums[l] >= nums[r]:

            #     r = mid -1 
            # elif  nums[l]<nums[r] and nums[mid] < target :
            #     l = mid+1 
            # elif  nums[l]<nums[r] and nums[mid] >target :
            #     r = mid -1 


            # else:
            #     return mid

"""
[4,5,6,7,0,1,2]
l = 0 , r = 6 mid = 4 , nums= 7 
if nums[mid] >target
l= 4 r = 6 mid= 5 nums = 1
if nums[mid] >target 
"""
        

        