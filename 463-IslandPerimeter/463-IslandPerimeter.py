class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        p  = 0 
        visit=set()

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 1
            if (r,c) in visit :
                return 0 
            # mark grid as visited 
            visit.add((r,c))
            p =dfs(r+1,c)
            p+=dfs(r-1,c)
            p+=dfs(r,c+1)
            p+=dfs(r,c-1)
            return p

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
      
                    return dfs(i, j)  # Start DFS to mark the entire island as visited

   


            

        