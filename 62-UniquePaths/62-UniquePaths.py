class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        from functools import lru_cache

        @lru_cache(None)
        def find(r, c):
            # Base case: if we reach the bottom-right corner, there's 1 unique path
            if r == m - 1 and c == n - 1:
                return 1

            # If out of bounds, return 0
            if r >= m or c >= n:
                return 0

            # Move down and right
            return find(r + 1, c) + find(r, c + 1)

        # Start from the top-left corner
        return find(0, 0)
