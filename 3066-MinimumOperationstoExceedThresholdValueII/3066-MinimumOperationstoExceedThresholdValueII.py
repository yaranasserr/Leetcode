class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # minheap 
        heapq.heapify(nums)
        ops = 0 

      
        while len(nums)>1 and nums[0] < k :
            x = heapq.heappop(nums)  # Smallest element
            y = heapq.heappop(nums)
            new_val=min(x,y)*2 +max(x,y)
            heapq.heappush(nums,new_val)
            ops+=1
        
        return ops

        

        # return (len(nums)-len(minheap))

        