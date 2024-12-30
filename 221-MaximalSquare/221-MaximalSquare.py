class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Top-down recursion with memoization
        rows = len(matrix)
        columns = len(matrix[0])
        cache = {}

        def maxs(r, c):
            # Base case: out of bounds
            if r >= rows or c >= columns:
                return 0
            # Check if the result is cached
            if (r, c) not in cache:
                # Recursive calls
                down = maxs(r + 1, c)
                right = maxs(r, c + 1)
                diagonal = maxs(r + 1, c + 1)

                # Cache the result for this cell
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diagonal)
                else:
                    cache[(r, c)] = 0

            return cache[(r, c)]

        # Start the recursion from (0, 0)
        for i in range(rows):
            for j in range(columns):
                maxs(i, j)
        
        # Return the maximum square area found
        return max(cache.values()) ** 2
