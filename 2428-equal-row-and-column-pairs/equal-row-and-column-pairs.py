class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
            n = len(grid)  # Size of the grid
            count = 0

            # Extract all columns
            columns = [[grid[row][col] for row in range(n)] for col in range(n)]

            # Compare each row with each column
            for row in grid:
                for column in columns:
                    if row == column:
                        count += 1

            return count
                
                
            