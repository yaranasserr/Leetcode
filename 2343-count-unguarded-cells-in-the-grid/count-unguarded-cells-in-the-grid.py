from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        grid = [[0 for _ in range(n)] for _ in range(m)]

        guard_set = {(x, y) for x, y in guards}
        wall_set = {(x, y) for x, y in walls}

        # Mark guards (1) and walls (-1)
        for i, j in guard_set:
            grid[i][j] = 1
        for i, j in wall_set:
            grid[i][j] = -1

        guarded = set()

        # Scan in straight lines from each guard
        def scan(r, c, dr, dc):
            while 0 <= r < m and 0 <= c < n:
                if (r, c) in guard_set or (r, c) in wall_set:
                    break
                guarded.add((r, c))
                r += dr
                c += dc

        # Start scanning in all directions from each guard
        for gr, gc in guards:
            for dr, dc in directions:
                scan(gr + dr, gc + dc, dr, dc)

        unguarded = (m * n) - len(guard_set) - len(wall_set) - len(guarded)
        return unguarded
