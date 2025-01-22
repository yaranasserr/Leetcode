from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, columns = len(isWater), len(isWater[0])
        height = [[-1] * columns for _ in range(rows)]  # Initialize all heights to -1
        queue = deque()

        # Initialize the queue with water cells
        for r in range(rows):
            for c in range(columns):
                if isWater[r][c] == 1:
                    height[r][c] = 0
                    queue.append((r, c))

        # BFS to calculate heights
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < columns and height[nr][nc] == -1:
                    height[nr][nc] = height[r][c] + 1
                    queue.append((nr, nc))

        return height
