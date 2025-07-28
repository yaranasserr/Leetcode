# Last updated: 7/28/2025, 3:00:24 PM
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        maximumones = 0 
        max_row_idx = 0 

         
        for r in range(m):
            ones= 0
            for c in range(n):
                
                if mat[r][c] == 1 :
                    ones+=1 


            if ones > maximumones :
                maximumones = ones
                max_row_idx= r 
            
        return[max_row_idx,maximumones]



        