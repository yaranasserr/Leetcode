
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        # assume each street has 4 directions
        #left , right , up , down
        # if == 1 there is direction 

        dirs = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        visited = set()

        def dfs(r, c):
            if (r, c) == (m - 1, n - 1):
                return True

            visited.add((r, c))

            for dr, dc in dirs[grid[r][c]]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    if (-dr, -dc) in dirs[grid[nr][nc]]:
                        if dfs(nr, nc):
                            return True

            return False

        return dfs(0, 0)