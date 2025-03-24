# Last updated: 3/24/2025, 12:37:24 PM
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda  x :x[0])
        # merge overlapping intervals 
        # [a,b][c,d]if c < b take min(a,c) , b =  max(b,d)
        print(meetings)
        res = [meetings[0]]
        for start,end in meetings :
            lastend = res[-1][1] # b 
            if start <= lastend :
                res[-1][1] = max(lastend,end)
            else:
                res.append([start,end])

        total = res[0][0] -1  # days before merging

        print(res)
        for i in range(1,len(res)) :
            _,endtime =res[i-1]
            starttime ,_= res[i]
            print((endtime,starttime))

            total += starttime - endtime -1 

        total += days - res[-1][1] # days after merging

        return total 






        