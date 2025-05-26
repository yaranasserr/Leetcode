from typing import List
from collections import defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)

        visit = set()   # nodes that are fully processed
        cycle = set()   # nodes in the current DFS path (for cycle detection)
        dp = {}         # cache: dp[node] = [count of colors a-z]

        def dfs(node):
            if node in cycle:
                return None  # cycle detected
            if node in visit:
                return dp[node]

            cycle.add(node)
            count = [0] * 26

            for nei in adj[node]:
                res = dfs(nei)
                if res is None:
                    return None  # cycle
                for i in range(26):
                    count[i] = max(count[i], res[i])

            color_idx = ord(colors[node]) - ord('a')
            count[color_idx] += 1

            dp[node] = count
            visit.add(node)
            cycle.remove(node)
            return count

        max_val = 0
        for node in range(n):
            res = dfs(node)
            if res is None:
                return -1  # cycle detected
            max_val = max(max_val, max(res))

        return max_val
