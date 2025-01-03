class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        columns = len(matrix[0])
        memo = [[-1 for _ in range(columns)] for _ in range(rows)]

        def dfs(r, c):
            if memo[r][c] != -1:  # Check if the result is already computed
                return memo[r][c]  # Return the cached result

            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            max_path = 0

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check boundaries and value condition
                if 0 <= nr < rows and 0 <= nc < columns and matrix[nr][nc] > matrix[r][c]:
                    max_path = max(max_path, dfs(nr, nc))

            memo[r][c] = 1 + max_path  # Store the result in memo
            return memo[r][c]

        # Iterate over all cells in the matrix
        max_length = 0
        for r in range(rows):
            for c in range(columns):
                max_length = max(max_length, dfs(r, c))

        return max_length
