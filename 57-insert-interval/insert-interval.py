class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = 0 
        r = len(intervals) -1 

        while l <= r :
            mid = (l+r)//2

            if intervals[mid][0] < newInterval[0]:
                l = mid+1
            else:
                r = mid-1

        intervals.insert(l,newInterval) # insert it at l 


        res = [intervals[0]]
        # check for overlapping 
        for start ,end in intervals[1:]:
            lastend = res[-1][1]

            if lastend >= start :
                res[-1][1] = max(end,lastend)

            else:
                res.append([start,end])

        return res 

            



        