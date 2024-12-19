from typing import List
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Building a graph
        adj = defaultdict(list)  # map a -> list of [b, a/b]

        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])

        # BFS function to evaluate a query
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1.0

            q, visit = deque(), set()
            q.append([src, 1.0])
            visit.add(src)

            while q:
                n, w = q.popleft()  # n: node, w: weight

                if n == target:
                    return w

                for nei, weight in adj[n]:
                    if nei not in visit:
                        q.append([nei, w * weight])
                        visit.add(nei)

            return -1.0

        # Process each query using BFS
        return [bfs(q[0], q[1]) for q in queries]
