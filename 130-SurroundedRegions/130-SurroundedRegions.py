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
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            # Boundary check and ensure it's an 'O'
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return
            # Mark 'O' as 'T' to protect it
            board[r][c] = "T"

            # Perform DFS in all four directions
            dfs(r, c + 1)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c - 1)

        # Step 1: Start DFS from all edge cells to protect boundary-connected 'O's
        for r in range(rows):
            for c in [0, cols - 1]:  # First and last column
                if board[r][c] == "O":
                    dfs(r, c)
        for c in range(cols):
            for r in [0, rows - 1]:  # First and last row
                if board[r][c] == "O":
                    dfs(r, c)

        # Step 2: Flip remaining 'O' to 'X', and protected 'T' back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":  # Surrounded region
                    board[r][c] = "X"
                elif board[r][c] == "T":  # Protected region
                    board[r][c] = "O"
