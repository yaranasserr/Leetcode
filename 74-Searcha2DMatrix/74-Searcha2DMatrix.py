class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == target:
                    return True
                
        return False