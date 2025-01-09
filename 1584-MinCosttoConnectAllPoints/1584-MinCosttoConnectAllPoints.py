import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}  # i : list of [cost ,node]

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([distance, j])
                adj[j].append([distance, i])

        # Prim's algorithm
        res = 0  # total cost
        visit = set()
        minH = [[0, 0]]  # min heap [cost, point]

        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue

            res += cost
            visit.add(i)
            for neicost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neicost, nei])

        return res
