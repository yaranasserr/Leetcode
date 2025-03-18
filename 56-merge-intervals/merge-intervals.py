from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        # Sort intervals by start time
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            a, b = res[-1]  # Last interval in the result
            c, d = intervals[i]

            if c <= b:  # Overlapping case
                res[-1] = [a, max(b, d)]
            else:  # Non-overlapping case
                res.append([c, d])

        return res
