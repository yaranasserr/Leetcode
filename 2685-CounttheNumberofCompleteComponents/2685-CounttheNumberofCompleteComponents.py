// Last updated: 3/22/2025, 2:08:39 PM
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # adj list 
        adj = {i:[] for i in range(n)}
        
        for a,b in edges :
            adj[a].append(b)
            adj[b].append(a)

        # search for cycles  {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [4], 4: [3], 5: []}
        # find connected components 
        def dfs(node,parent):
            visit.add(node)
            component.append(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei,node)

        visit= set()
        components= []

        for v in range(n):
            if v not in visit :
                component = []
                dfs(v,component)
                components.append(component)

        # counting edges 
        #[[0, 1, 2], [3, 4, 5]]
        #{0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [4, 5], 4: [3], 5: [3]}
        # for each i in component  , its length of key of adj list =2 -> edge 
        edges = []
        for c in components :
            count = 0 
            for v in c :
                count +=len(adj[v])
            edges.append(count//2)
                
        print(edges)






        count = 0 

        for e,c in zip(edges,components) :
           
            m=len(c) # nodes 
            eqn= (m*(m-1))//2  
        
            if  e== eqn :
                count +=1

        return count

    

        


     

         


                




        