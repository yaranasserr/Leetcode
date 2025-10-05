# Last updated: 10/5/2025, 5:20:17 PM
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl , pac = set(),set()
        m,n = len(heights),len(heights[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        res = []
     

        def dfs(r,c,visit,prevh):
            if r <0 or c<0 or r >= m or c>=n or (r,c) in visit or heights[r][c]< prevh:
                return
            visit.add((r,c))


            for dr , dc in directions :
                dfs(r+dr,c+dc,visit,heights[r][c])

        
        for r in range(m):
            dfs(r,0,pac,heights[r][0]) # left , pac 
            dfs(r,n-1,atl,heights[r][n-1]) # right  .,atl

        for c in range(n):
            dfs(0,c,pac,heights[0][c]) # top , pac
            dfs(m-1,c,atl,heights[m-1][c]) # bottom ,atl

        for r in range(m):
            for c in range(n):
                if (r,c) in pac and (r,c) in atl :
                    res.append([r,c])

        return res

        


        