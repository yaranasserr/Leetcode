class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        # line sweep and minheap 
        intervals.sort()
        minheap=[]
        res , i = {} , 0 
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q :
                l,r = intervals[i]
                heapq.heappush(minheap,(r-l+1,r)) # size of heap , right of heap 
                i+=1 
            # too far interval , right value of interval < q 

            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)

            res[q]=minheap[0][0] if minheap else -1 

        return [res[q] for q in queries] 

        