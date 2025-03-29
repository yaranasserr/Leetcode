# Last updated: 3/29/2025, 11:54:37 PM
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Modify board in-place to reflect the next state of Conway's Game of Life.
        """
        if not board:
            return
        
        m, n = len(board), len(board[0])

        def count_live_neighbors(r, c):
            """Counts the number of live (1) neighbors around (r, c)."""
            neighbours = [
                (0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)
            ]
            count = 0
            for dr, dc in neighbours:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and abs(board[nr][nc]) == 1:
                    count += 1
            return count


        for r in range(m):
            for c in range(n):
                live_neighbors = count_live_neighbors(r, c)
                
                # Rule 1 & 3: Live cell dies if <2 or >3 live neighbors
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1  
                
                # Rule 4: Dead cell with exactly 3 live neighbors becomes live
                elif board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2  # Mark as live (previously dead)
        
        # Second pass: Apply changes
        for r in range(m):
            for c in range(n):
                if board[r][c] == -1:  # Previously live, now dead
                    board[r][c] = 0
                elif board[r][c] == 2:  # Previously dead, now live
                    board[r][c] = 1
