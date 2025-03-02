# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         res = []
#         l = 0 
#         r= k 

#         while r <= len(nums):
#             maxheap = [[-num,i]  for i , num in enumerate(nums[l:r],start = l)]
#             heapq.heapify(maxheap)
#             # sort the maxheap by the value [0], and put the index too[1]

#             # get index of the max num check if still in window
#             while maxheap[0][1] < l :
#                 heapq.heappop(maxheap)

#             res.append(-maxheap[0][0]) # append the value 
#             l+=1
#             r+=1

#         return res

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output


        