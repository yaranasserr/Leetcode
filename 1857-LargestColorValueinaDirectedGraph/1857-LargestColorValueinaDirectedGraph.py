# Last updated: 5/26/2025, 3:52:13 PM
from typing import List
from collections import defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)

        visit = set()
        cycle = set()
        has_cycle = False
        dp = [[0] * 26 for _ in range(n)]  # dp[node][color]

        def dfs(node):
            nonlocal has_cycle
            if node in cycle:
                has_cycle = True
                return
            if node in visit:
                return

            cycle.add(node)
            for nei in adj[node]:
                dfs(nei)
                if has_cycle:
                    return
                for c in range(26):
                    dp[node][c] = max(dp[node][c], dp[nei][c])
            # add this node's own color
            dp[node][ord(colors[node]) - ord('a')] += 1
            cycle.remove(node)
            visit.add(node)

        for node in range(n):
            if node not in visit:
                dfs(node)
                if has_cycle:
                    return -1

        return max(max(counts) for counts in dp)
