from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> List[List[List[int]]]:
        def canSplit(largest):
                subarray = 1
                curSum = 0
                for n in nums:
                    curSum += n
                    if curSum >largest:
                        subarray +=1 
                        curSum = n 

                return subarray <= m 
        l,r = max(nums) , sum(nums)
        res = r 
              

        # use binary search

        while l <= r:
            mid = (l+r) //2

            if canSplit(mid):
                res = mid 
                r = mid -1
            else:
                l = mid+1 
        return res

      

        
        # # Helper function to generate all combinations
        # def helper(nums, k, start, current_split, result):
        #     if k == 1:  # Only one part left, it must take the rest of the array
        #         result.append(current_split + [nums[start:]])
        #         return
        #     for i in range(start + 1, len(nums) - k + 2):  # Ensure each part has at least one element
        #         helper(nums, k - 1, i, current_split + [nums[start:i]], result)
        # result = []
        # helper(nums, k, 0, [], result)
        # def sum_of_subarrays(result):
        # # Calculate the sum of each subarray in the result
        #     sum_result = []
        #     for split in result:
        #         sum_split = [sum(subarray) for subarray in split]
        #         sum_result.append(sum_split)
        #     return sum_result

        # sums = sum_of_subarrays(result)
        # maximum = []
        # for i in sums  :
        #     maximum.append(max(i))

        # return min(maximum)

        
 
        