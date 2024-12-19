class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited=set()
        provinces =0 

        def dfs(city):
            visited.add(city)
            #[[1,1,0],[1,1,0],[0,0,1]]
            # cur : 0,1,2 connected : 1,1,0
            for cur , connected in enumerate(isConnected[city]):
                if connected and cur  not in visited:
                    dfs(cur) #cur is new city 


        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provinces +=1
        return provinces 
 
        