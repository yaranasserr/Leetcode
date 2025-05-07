# Last updated: 5/7/2025, 5:42:37 PM
import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        m, n = len(moveTime), len(moveTime[0])
        dir = [-1, 0, 1, 0, -1]
        
        def isValid(r, c, m, n):
            return 0 <= r < m and 0 <= c < n

        minHeap = [(0, 0, 0)]  # (time, row, col)
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        while minHeap:
            time, r, c = heapq.heappop(minHeap)

            if r == m - 1 and c == n - 1:
                return time

            for i in range(4):
                newR, newC = r + dir[i], c + dir[i + 1]

                if isValid(newR, newC, m, n) and not visited[newR][newC]:
                    newTime = 1 + max(time, moveTime[newR][newC])
                    heapq.heappush(minHeap, (newTime, newR, newC))
                    visited[newR][newC] = True

        return -1