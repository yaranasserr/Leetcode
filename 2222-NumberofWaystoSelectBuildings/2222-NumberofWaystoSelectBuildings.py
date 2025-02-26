class Solution:
    def numberOfWays(self, s: str) -> int:
        # Helper function to find number of subsequences of 'sub' in 's'
        def dp(s, sub):
            n1 = len(s)
            n2 = len(sub)
            grid = [[0] * (n2 + 1) for _ in range(n1 + 1)]

            for i in range(n1 + 1):
                grid[i][n2] = 1

            # Fill DP table bottom-up
            for i in range(n1 - 1, -1, -1):
                for j in range(n2 - 1, -1, -1):
                    # Move to the next character in 'sub' if it matches
                    if s[i] == sub[j]:
                        grid[i][j] = grid[i + 1][j + 1] + grid[i + 1][j]
                    else:
                        grid[i][j] = grid[i + 1][j]

            return grid[0][0]

       
        return dp(s, '101') + dp(s, '010')


