# from typing import List

# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         if not board:
#             return

#         rows, cols = len(board), len(board[0])

#         def dfs(r, c):
#             # Ensure the current cell is within bounds, is 'O', and not on the edge
#             if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
#                 return
#             if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
#                 return
            
#             # Mark the current cell as visited by changing 'O' to 'X'
#             board[r][c] = "X"

#             # Perform DFS in all four directions
#             dfs(r, c + 1)
#             dfs(r + 1, c)
#             dfs(r - 1, c)
#             dfs(r, c - 1)

#         for r in range(rows):
#             for c in range(cols):
#                 if board[r][c] == "O":
#                     dfs(r, c)
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            # Skip if out of bounds or not 'O'
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return
            # Mark as visited by replacing 'O' with a placeholder ('#')
            board[r][c] = "#"
            # Explore neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Start DFS from all edge 'O's
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)  # Left edge
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)  # Right edge
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)  # Top edge
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)  # Bottom edge
        
        # Flip all remaining 'O's to 'X', and restore '#' to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"

# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         if not board or not board[0]:
#             return

#         rows, cols = len(board), len(board[0])

#         def dfs(r, c):
#             # Boundary check and ensure it's an 'O'
#             if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
#                 return
#             # Mark 'O' as 'T' to protect it
#             board[r][c] = "T"

#             # Perform DFS in all four directions
#             dfs(r, c + 1)
#             dfs(r + 1, c)
#             dfs(r - 1, c)
#             dfs(r, c - 1)

#         # Step 1: Start DFS from all edge cells to protect boundary-connected 'O's
#         for r in range(rows):
#             for c in [0, cols - 1]:  # First and last column
#                 if board[r][c] == "O":
#                     dfs(r, c)
#         for c in range(cols):
#             for r in [0, rows - 1]:  # First and last row
#                 if board[r][c] == "O":
#                     dfs(r, c)

#         # Step 2: Flip remaining 'O' to 'X', and protected 'T' back to 'O'
#         for r in range(rows):
#             for c in range(cols):
#                 if board[r][c] == "O":  # Surrounded region
#                     board[r][c] = "X"
#                 elif board[r][c] == "T":  # Protected region
#                     board[r][c] = "O"
