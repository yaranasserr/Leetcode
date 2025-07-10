# Last updated: 7/10/2025, 6:10:48 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # search in first and last cols to locate the targeted row 
        # then do bs in row 
        boundaries = {}

        for r in range(m):
            boundaries[r] = [matrix[r][0], matrix[r][n - 1]]

        l = 0 
        r = n-1
        row = -1

        for r,(x,y) in boundaries.items():
            if x <= target <= y :
                row = r 
                break 

        if row == -1:
            return False 

        l = 0 
        r = n-1 
        target_row = matrix[row]

        while l <= r :
            mid = (l+r)//2 
            if target_row[mid] == target :
                return True 

            elif target_row[mid] < target :
                l = mid+1
            else:
                r = mid -1 

        return False 

        