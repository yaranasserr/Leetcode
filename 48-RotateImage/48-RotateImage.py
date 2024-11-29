import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
      

    #First Transpose matrix
   
        
    
        n=len(matrix)
        startC=0
        for r in range(n):
            for c in range(startC,n):
                matrix[r][c] , matrix[c][r] = matrix[c][r] , matrix[r][c]
            startC+=1
            
            
            
         #second swap the columns
       
        nColSwap=n//2
        for c in range(nColSwap):
            for r in range(n):
                 matrix[r][c],matrix[r][n-c-1]=matrix[r][n-c-1],matrix[r][c]
                    

            
        
      
          
       
     
     
       
          
            