from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        # two pointers 
        n = len(nums)
        count = 1
        if n == 1:
            return True 
            
        for i in range(1,2*n):
            if nums[(i-1)%n] <= nums[i%n]:
                count +=1
            else :
                count = 1 

            if count == n :
                return True 
        return False 
        # dq = deque(nums)
    
        # for _ in range(len(nums)):  
        #     if list(dq) == sorted(dq): 
        #         return True
        #     dq.append(dq.popleft())  
        
        # return False


            
        # count_drops = 0
        # n = len(nums)
        
        # for i in range(n):
        #     if nums[i] > nums[(i + 1) % n]:  
        #         count_drops += 1
        #         if count_drops > 1: 
        #             return False
        
        # return True
