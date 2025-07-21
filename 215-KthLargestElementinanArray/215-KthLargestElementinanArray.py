# Last updated: 7/21/2025, 3:06:32 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for n in nums :
            heapq.heappush(minheap,n)

            if len(minheap)> k :
                heapq.heappop(minheap)

        return minheap[0]
        