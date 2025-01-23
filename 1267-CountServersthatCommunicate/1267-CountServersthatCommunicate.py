class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        res=[]
        # row as index and no of servers as count 
        row_count = [0]*rows
        column_count = [0]*columns

        for i in range(rows):
            for j in range(columns):
                if grid[i][j]:
                    row_count[i]+=1
                    column_count[j] +=1 

        res = 0 
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] and (max(row_count[i],column_count[j]) > 1 ):
                    res +=1

        return res






        