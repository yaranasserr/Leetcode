# Last updated: 3/30/2025, 5:41:13 PM
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        available =[i for i in range(n)]
        
        used = [] # end_time , room no
        count=[0]*n # count[n] :meetings schdeuled 
        # meeting room has most meeting schedulded
        for start,end in meetings:
            # finish meetings 
            # which meeting has the smallest end time
            while used and start >=used[0][0]:
                _,room=heapq.heappop(used)
                heapq.heappush(available,room)
            # no room is aval
            # pop from used and pput meeing
            if not available:
                end_time,room=heapq.heappop(used)
                end = end_time+(end-start)
                heapq.heappush(available,room)

            room=heapq.heappop(available)
            heapq.heappush(used,(end,room))

            count[room] +=1

            # room is available 

        

        return count.index(max(count))


        
        