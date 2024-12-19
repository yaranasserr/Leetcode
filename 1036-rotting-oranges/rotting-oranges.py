from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        rows, columns = len(grid), len(grid[0])

        # Count fresh oranges and add rotten ones to the queue
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # BFS to rot oranges
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()  # Coordinates of a rotten orange
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    # Check bounds and if the orange is fresh
                    if (
                        row < 0
                        or row >= rows
                        or col < 0
                        or col >= columns
                        or grid[row][col] != 1
                    ):
                        continue
                    # Make the fresh orange rotten
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1

            time += 1  # Increment time after processing one level

        # Return time if all fresh oranges are rotten, otherwise -1
        return time if fresh == 0 else -1
