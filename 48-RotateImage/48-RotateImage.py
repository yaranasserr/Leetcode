# Last updated: 5/4/2026, 11:39:22 AM
1import numpy as np
2class Solution:
3    def rotate(self, matrix: List[List[int]]) -> None:
4        """
5        Do not return anything, modify matrix in-place instead.
6        """
7      
8
9    #First Transpose matrix
10   
11        
12    
13        n=len(matrix)
14        startC=0
15        for r in range(n):
16            for c in range(startC,n):
17                matrix[r][c] , matrix[c][r] = matrix[c][r] , matrix[r][c]
18            startC+=1
19            
20            
21            
22         #second swap the columns
23       
24        nColSwap=n//2
25        for c in range(nColSwap):
26            for r in range(n):
27                 matrix[r][c],matrix[r][n-c-1]=matrix[r][n-c-1],matrix[r][c]
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