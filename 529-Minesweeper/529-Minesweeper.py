from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        r, c = click
        
        # Directions for the 8 possible adjacent squares
        directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        
        def count_mines(r, c):
            """Counts the number of mines adjacent to (r, c)."""
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "M":
                    count += 1
            return count
        
        def dfs(r, c):
            """Recursive DFS to reveal adjacent squares."""
            if not (0 <= r < m and 0 <= c < n) or board[r][c] != 'E':
                return
            
            mine_count = count_mines(r, c)
            if mine_count > 0:
                board[r][c] = str(mine_count)  # Convert mine count to a string digit
            else:
                board[r][c] = 'B'
                for dr, dc in directions:
                    dfs(r + dr, c + dc)
        
        # Handle the click position
        if board[r][c] == "M":  # Mine clicked -> Game Over
            board[r][c] = "X"
        else:  # Reveal empty or numbered square
            dfs(r, c)
        
        return board
