class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.current_tasks={}
        self.heap= []
        for u,t,p in tasks:
            self.current_tasks[t]=(p,u)
            heapq.heappush(self.heap,(-p,-t,u))

        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.current_tasks[taskId]=(priority,userId)
        heapq.heappush(self.heap,(-priority,-taskId,userId))
        


    def edit(self, taskId: int, newPriority: int) -> None:
        currentpriority,current_userid=self.current_tasks[taskId] # get p , u from dict 
        self.current_tasks[taskId] = (newPriority,current_userid)
        heapq.heappush(self.heap,(-newPriority,-taskId,current_userid))




        

    def rmv(self, taskId: int) -> None:
        del self.current_tasks[taskId]

    def execTop(self) -> int:
        while self.heap:
            priority, taskId, userId = heapq.heappop(self.heap)
            priority, taskId = abs(priority), abs(taskId)

            if taskId not in self.current_tasks or self.current_tasks[taskId][0] != priority or self.current_tasks[taskId][1] != userId:
                continue

            del self.current_tasks[taskId]
            return userId

        return -1

        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()