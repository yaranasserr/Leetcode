# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         res = [-1]*len(nums2)
#         stack = []
#         ans = []

#         # hashmap
#         hashmap = {i:[] for i in nums1}
#         for i in hashmap:
#             hashmap[i]=nums2.index(i)

#         # monotonic stack for nums2
#         res = [-1]*len(nums2)
#         stack = []
#         for j in range(len(nums2)-1,-1,-1):
#             while stack and stack[-1] <= nums2[j]:
#                 stack.pop()
#             if stack :
#                 res[j]=stack[-1]
#             stack.append(nums2[j])

#          # {4: [ 2], 1: [ 0], 2: [ 3]}
#         for i in hashmap.values():
#             ans.append(res[i])

#         return ans
            

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        
        # Compute next greater element for each number in nums2 using a monotonic stack
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            next_greater[num] = stack[-1] if stack else -1
            stack.append(num)
        
        # Map results for nums1 based on nums2's next greater element mapping
        return [next_greater[num] for num in nums1]






        