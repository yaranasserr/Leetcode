# Last updated: 12/31/2025, 3:32:00 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        islands = 0 
4        m , n = len(grid) , len(grid[0])
5
6        directions = [[0,1],[0,-1],[1,0],[-1,0]]
7
8        def dfs(r,c):
9            if r < 0 or c<0 or r >= m or c>= n or grid[r][c] == "0":
10                return 
11
12            grid[r][c] = "0"
13
14            for dr ,dc in directions :
15                dfs(dr+r,dc+c)
16
17
18
19        for i in range(m):
20            for j in range(n):
21                if grid[i][j] =="1":
22                    islands +=1
23                    dfs(i,j)
24
25        return islands  
26
27        
28
29
30
31
32
33        
34
35
36
37
38            
39
40
41        
42        