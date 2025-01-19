from heapq import heappush, heappop

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        rows, cols = len(heightMap), len(heightMap[0])
        visited = [[False] * cols for _ in range(rows)]
        min_heap = []
        trapped_water = 0

        # Step 1: Add all boundary cells to the heap
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    heappush(min_heap, (heightMap[r][c], r, c))
                    visited[r][c] = True

        # Step 2: Process cells in the heap
        while min_heap:
            height, r, c = heappop(min_heap)

            # Check 4 neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # Water trapped at this cell
                    trapped_water += max(0, height - heightMap[nr][nc])
                    # Push the updated height into the heap
                    heappush(min_heap, (max(height, heightMap[nr][nc]), nr, nc))

        return trapped_water
           
                