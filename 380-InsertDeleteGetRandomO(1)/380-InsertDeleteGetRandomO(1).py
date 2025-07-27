# Last updated: 7/27/2025, 2:04:58 PM
class Solution:
    def totalNQueens(self, n: int) -> int:
        counter = 0

        def backtrack(r, cols, diagonals, antidiagonals):
            nonlocal counter
            if r == n:
                counter += 1
                return
            for c in range(n):
                if c in cols or (r + c) in antidiagonals or (r - c) in diagonals:
                    continue
                cols.add(c)
                antidiagonals.add(r + c)
                diagonals.add(r - c)
                backtrack(r + 1, cols, diagonals, antidiagonals)
                cols.remove(c)
                antidiagonals.remove(r + c)
                diagonals.remove(r - c)

        backtrack(0, set(), set(), set())
        return counter