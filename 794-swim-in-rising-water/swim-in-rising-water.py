import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()
        minheap = [(grid[0][0], 0, 0)]  # (time, row, col)

        visit.add((0, 0))

        while minheap:
            t, r, c = heapq.heappop(minheap)
            if r == n - 1 and c == n - 1:
                return t

            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (
                    neiR < 0
                    or neiC < 0
                    or neiR >= n
                    or neiC >= n   
                    or (neiR, neiC) in visit
                ):
                    continue

                visit.add((neiR, neiC))
                heapq.heappush(minheap, (max(t, grid[neiR][neiC]), neiR, neiC))
