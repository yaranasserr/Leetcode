import collections
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols= len(heights[0])

        def dfs(r,c,visit,prevheight):
            if(r,c) in visit or  r< 0 or c<0 or r== rows or c == cols or heights[r][c] < prevheight:
                return 
            visit.add((r,c))

            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])


        pac , atl = set() , set()
        # every (column) positon in first row
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])  # first row
            dfs(rows-1,c,atl,heights[rows-1][c]) # last row 

        for r in range(rows):
            dfs(r,0,pac,heights[r][0]) # first column
            dfs(r,cols-1,atl,heights[r][cols-1]) # lst column

        res=[]

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res








      
       