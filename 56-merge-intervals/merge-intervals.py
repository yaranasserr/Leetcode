from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        # Sort intervals by start time
        intervals.sort(key = lambda i :i[0]) # sort by start of interval 
        res = [intervals[0]]

        for start,end in intervals[1:]:
            lastend = res[-1][1]

            if start <= lastend :
                res[-1][1] = max(lastend,end)
            else:
                res.append([start,end])

        return res

           