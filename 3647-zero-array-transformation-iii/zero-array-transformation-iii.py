from typing import List

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        queries.sort(key=lambda i: i[0])  
        heap = []
        deltaarray = [0] *(n+1)
        ops = 0 
        j = 0 
        for i , num in enumerate(nums):
            ops +=deltaarray[i]
            while j < len(queries) and queries[j][0] == i :
                heappush(heap,-queries[j][1])
                j+=1
            while ops < num and heap and -heap[0] >= i :
                ops+=1
                deltaarray[-heappop(heap)+1] -=1
            if ops < num :
                return -1 
        return len(heap)


        # used = 0 
        # for a, b in queries:
          
        #     for i in range(a, b + 1):
        #         if nums[i] > 0:
        #             nums[i] -= 1
        #     used += 1
           
            
        #     if all(x == 0 for x in nums):
        #         break  

    
        # res = len(queries) - used
        # return res if all(x == 0 for x in nums) else -1
