# Last updated: 11/28/2025, 6:38:33 PM
1class Solution:
2    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
3        adj= defaultdict(list)
4        
5        for n1,n2 in edges:
6            adj[n1].append(n2)
7            adj[n2].append(n1)
8
9        res = 0 
10
11        def dfs(cur,par):
12            total = values[cur]
13            for child in adj[cur]:
14                if child != par :
15                    total +=dfs(child,cur)
16
17            if total%k ==0 :
18                nonlocal res 
19                res+=1
20            return total 
21
22        dfs(0,-1)
23        return res 