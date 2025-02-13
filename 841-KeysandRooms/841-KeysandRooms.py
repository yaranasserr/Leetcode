class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visit = set()
        prov = 0 

        def dfs(city):
            visit.add(city)
            for cur , nei in enumerate(isConnected[city]):
                if nei and cur not in visit :
                    dfs(cur)

        for i in range(len(isConnected)):
            if i not in visit:
                dfs(i)
                prov+=1
        return prov

        





            





 
        