from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        columns = len(matrix[0])
        memo = [[-1 for _ in range(columns)] for _ in range(rows)]

        def dfs(r, c):
            # Base case: check if out of bounds or already computed
            if r < 0 or r >= rows or c < 0 or c >= columns:
                return 0
            if memo[r][c] != -1:  # If the result is already computed
                return memo[r][c]

            # Directions: down, right, up, left
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            max_path = 0

            # Check each direction (down, right, up, left)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Skip if the next cell is out of bounds or has a smaller or equal value
                if nr < 0 or nr >= rows or nc < 0 or nc >= columns or matrix[nr][nc] <= matrix[r][c]:
                    continue

                # Recursively find the longest increasing path from the neighboring cell
                max_path = max(max_path, dfs(nr, nc))

            # Memoize the result for the current cell (1 + max path from neighbors)
            memo[r][c] = 1 + max_path
            return memo[r][c]

        # Find the longest increasing path by calling DFS on each cell
        max_length = 0
        for r in range(rows):
            for c in range(columns):
                max_length = max(max_length, dfs(r, c))

        return max_length
