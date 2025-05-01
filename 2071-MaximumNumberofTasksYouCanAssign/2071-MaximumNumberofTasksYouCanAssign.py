# Last updated: 5/1/2025, 4:16:11 PM
from sortedcontainers import SortedList
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:

        n = len(tasks)
        m = len(workers)
        # # binary search 
        tasks.sort()
        workers.sort()
        def check(mid):
            p = pills
            ws = SortedList(workers[m-mid:])

            for i in range(mid-1,-1,-1):
                if ws[-1] >= tasks[i]:
                    ws.pop()
                else:
                    if p == 0 :
                        return False 
                    rep = ws.bisect_left(tasks[i]-strength)
                    if rep == len(ws):
                        return False 
                    p -=1
                    ws.pop(rep)
            return True 

        left , right , ans = 1 , min(m,n) , 0 
        while left <= right :
            mid = (left+right)//2 
            if check(mid):
                ans = mid 
                left = mid+1
            else:
                right = mid -1
        return ans 


        # low = 0 
        # high = min(m,n)
        # ans = 0 
        # def check(k,tasks,workers,pills,strength):
        #     n = len(tasks)
        #     m = len(workers)
        #     current_workers = deque(workers[m-k:])
        #     pills_left = pills

        #     for i in range(k-1,-1,-1):
        #         task_strength = tasks[i]

        #         if current_workers[-1] >= task_strength :
        #             current_workers.pop()
        #         elif pills_left > 0 and current_workers[0] + strength >= task_strength :
        #             pills_left -=1
        #             current_workers.popleft()

        #         else:
        #             return False 

        #     return True 


        # while low<= high :
        #     k = (low+high) // 2 

        #     if k == 0 :
        #         ans = k  # try more 
        #         low = k+1
        #         continue 
        #     if check(k,tasks,workers,pills,strength):
        #         ans = k 
        #         low = k+1
        #     else:
        #         high = k -1

        # return ans 



        