# Last updated: 9/18/2025, 1:54:46 PM
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.current_tasks = {} # taskid-> p, user 
        self.heap = []
        for u,t,p in tasks:
            self.current_tasks[t] =(p,u)
            heapq.heappush(self.heap,(-p,-t,u)) # max heap
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.current_tasks[taskId]=(priority,userId)
        heapq.heappush(self.heap,(-priority,-taskId,userId))
        

    def edit(self, taskId: int, newPriority: int) -> None:
        current_p , current_u = self.current_tasks[taskId]
        self.current_tasks[taskId] = (newPriority,current_u)
        heapq.heappush(self.heap,(-newPriority,-taskId,current_u))


    def rmv(self, taskId: int) -> None:
        del self.current_tasks[taskId]
        

    def execTop(self) -> int:
        while self.heap :
            p,t,u = heapq.heappop(self.heap)
            p,t = abs(p),abs(t)

            if t not in self.current_tasks or self.current_tasks[t][0] != p or self.current_tasks[t][1] != u :
                continue 

            del self.current_tasks[t]
            return u 

        return -1 
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()