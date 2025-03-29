# Last updated: 3/29/2025, 11:55:24 PM
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        l= 0
        r = len(intervals) -1
    

        while l <= r :
            mid = (l+r )//2

            if intervals[mid][0] < newInterval[0]:
                l = mid +1
            else:
                r = mid -1 

        # mid is where the new interval will be places 

        intervals.insert(l,newInterval)
        
        
        # merge intervals
        res = [intervals[0]]

        for start , end in intervals[1:]:
            lastend = res[-1][1]

            if start <= lastend:
                res[-1][1]=max(end,lastend)
            else:
                res.append([start,end])

        return res

        

        
        