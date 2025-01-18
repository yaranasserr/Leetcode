from collections import deque
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
    
        rows = len(grid)
        columns = len(grid[0])

        # 1: right, 2: left, 3: down, 4: up
        direction = {
            1: [0, 1],  
            2: [0, -1], 
            3: [1, 0], 
            4: [-1, 0] 
        }

        q = deque([(0, 0, 0)])  # (row, column, cost)
       
        min_cost = {(0, 0): 0}  # (row, column) -> cost

        # Perform BFS
        while q:
            r, c, cost = q.popleft()

          
            if (r, c) == (rows - 1, columns - 1):
                return cost

   
            for d in direction:
                dr, dc = direction[d]
                nr, nc = r + dr, c + dc  
                # Calculate the cost to move to the new cell
                n_cost = cost if d == grid[r][c] else cost + 1

       
                if (
                    nr < 0 or nc < 0 or nr == rows or nc == columns or 
                    n_cost >= min_cost.get((nr, nc), float("inf"))
                ):
                    continue

                # Update the minimum cost for the new cell
                min_cost[(nr, nc)] = n_cost

                # Prioritize cells where no additional cost is incurred
                if d == grid[r][c]:
                    q.appendleft((nr, nc, n_cost))
                else:
                    q.append((nr, nc, n_cost))

        return float("inf")
