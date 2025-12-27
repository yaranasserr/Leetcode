# Last updated: 12/27/2025, 1:51:58 PM
1class Solution:
2    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
3        meetings.sort(key=lambda x:x[0])
4        available =[i for i in range(n)]
5        
6        used = [] # end_time , room no
7        count=[0]*n # count[n] :meetings schdeuled 
8        # meeting room has most meeting schedulded
9        for start,end in meetings:
10            # finish meetings 
11            # which meeting has the smallest end time
12            while used and start >=used[0][0]:
13                _,room=heapq.heappop(used)
14                heapq.heappush(available,room)
15            # no room is aval
16            # pop from used and pput meeing
17            if not available:
18                end_time,room=heapq.heappop(used)
19                end = end_time+(end-start)
20                heapq.heappush(available,room)
21
22            room=heapq.heappop(available)
23            heapq.heappush(used,(end,room))
24
25            count[room] +=1
26
27            # room is available 
28
29        
30
31        return count.index(max(count))
32
33
34        
35        