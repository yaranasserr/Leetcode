# Last updated: 5/21/2025, 4:51:32 AM
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rows = [False]*m
        cols = [False]*n

        for r in range(m) :
            for c in range(n):
                if matrix[r][c] == 0 :
                    rows[r]=True 
                    cols[c]=True 

        for r in range(m):
            for c in range(n):
                if rows[r]:
                    matrix[r][c] = 0 
                elif cols[c]:
                    matrix[r][c] = 0 

    
        