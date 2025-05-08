# Last updated: 5/8/2025, 8:52:49 PM
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        ROWS, COLS = len(moveTime), len(moveTime[0])

        cache = [[inf]*COLS for _ in range(ROWS)]
        cache[0][0] = 0

        min_heap = [] 
        heappush(min_heap, (0, 0, 0, 0))

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while min_heap:
            t, r, c, steps = heappop(min_heap)

            if r == ROWS - 1 and c == COLS - 1:
                return t

            for dr, dc in directions:
                r_new = r + dr
                c_new = c + dc

                if not((0 <= r_new < ROWS) and (0 <= c_new < COLS)):
                    continue 
                
                move_time = (1 if (steps % 2 == 0) else 2)
                new_time = max(t, moveTime[r_new][c_new]) + move_time

                if new_time < cache[r_new][c_new]:
                    cache[r_new][c_new] = new_time
                    heappush(min_heap, (new_time, r_new, c_new, steps + 1))