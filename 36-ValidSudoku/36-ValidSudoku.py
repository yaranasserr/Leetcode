# Last updated: 3/29/2025, 11:54:06 PM
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res =  []
        top=left = 0 
        bottom = len(matrix)
        right = len(matrix[0]) # last col

        while left < right and top < bottom :
            # top from left to right
            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1
            # right col from top to bottom 
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right -=1 

            if not (left<right and top < bottom):
                break

            # bottom (right to left)
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom -=1 

            # left col from bottom to top 
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left +=1

        return res 
        