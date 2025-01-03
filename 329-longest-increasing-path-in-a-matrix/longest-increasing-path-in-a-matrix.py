from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # O(n) = n*m
        rows = len(matrix)
        columns = len(matrix[0])
        memo = {}

        def dfs(r, c,prev):
            if r < 0 or r == rows or c < 0 or c == columns or matrix[r][c] <= prev :
                return 0 

            if (r,c) in memo:
                return memo[(r,c)]

      
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]       #  down, right, up, left
            res = 0 
            for dr ,dc in directions:
                res = max(res,1+dfs(r+dr,c+dc,matrix[r][c]))
            memo[(r,c)] =res

            return res
        
        for r in range(rows):
            for c in range(columns):
                dfs(r,c,-1)
        return max(memo.values())
                

# from typing import List

# class Solution:
#     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
#         # O(n) = n*m
        
#         rows = len(matrix)
#         columns = len(matrix[0])
#         memo = [[-1 for _ in range(columns)] for _ in range(rows)]

#         def dfs(r, c):
#             if r < 0 or r >= rows or c < 0 or c >= columns:
#                 return 0
#             if memo[r][c] != -1: 
#                 return memo[r][c]
      
#             directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]       #  down, right, up, left
#             max_path = 0

#             for dr, dc in directions:
#                 nr, nc = r + dr, c + dc

#                 # Skip if the next cell is out of bounds or has a smaller or equal value
#                 if nr < 0 or nr >= rows or nc < 0 or nc >= columns or matrix[nr][nc] <= matrix[r][c]:
#                     continue
#                 max_path = max(max_path, dfs(nr, nc))

#             memo[r][c] = 1 + max_path

#             return memo[r][c]
#         max_length = 0
#         for r in range(rows):
#             for c in range(columns):
#                 max_length = max(max_length, dfs(r, c))

#         return max_length
