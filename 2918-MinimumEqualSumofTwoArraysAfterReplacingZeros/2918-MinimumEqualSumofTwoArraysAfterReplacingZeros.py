# Last updated: 5/10/2025, 4:06:28 PM
from typing import List
from collections import Counter

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
       
        c1 , c2  = Counter(nums1) ,Counter(nums2)
 
        z1 , z2 = c1.get(0, 0) ,c2.get(0, 0)

        sum1 , sum2 = 0,0 
         # the answer will be -1 if there was no 0 in the array with the smaller sum of elements.
       
        for i in nums1:
            sum1 += i 
            if i == 0 :
                sum1+=1

        for i in nums2:
            sum2  += i 
            if i == 0 :
                sum2 +=1 

        if (sum2 > sum1 and z1 == 0) or (sum1>sum2 and z2 == 0):
            return -1


        return max(sum1,sum2)

        # # add ones to the array with less sum
        # if z1 < z2 and sum(nums1)>sum(nums2) :
        #     nums1_new = [1 if x == 0 else x for x in nums1]
        #     total_1 = sum(nums1_new)
         
        #     return total_1
        
        # else:
        #     nums2_new = [1 if x==0 else x for x in nums2]
        #     total_2 = sum(nums2_new)
       
        #     return total_2
            




        
