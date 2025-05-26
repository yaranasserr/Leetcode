# Last updated: 5/26/2025, 3:59:33 PM
from typing import List
from collections import defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)

        visited = [0] * n  # 0 = unvisited, 1 = visiting, 2 = visited
        dp = [None] * n    # dp[node] = color frequency list at that node
        has_cycle = False

        def dfs(node):
            nonlocal has_cycle
            if visited[node] == 1:  # cycle detected
                has_cycle = True
                return [0] * 26
            if visited[node] == 2:  # already visited
                return dp[node]

            visited[node] = 1
            count = [0] * 26

            for nei in adj[node]:
                res = dfs(nei)
                if has_cycle:
                    return [0] * 26
                for i in range(26):
                    count[i] = max(count[i], res[i])

            color_index = ord(colors[node]) - ord('a')
            count[color_index] += 1

            visited[node] = 2
            dp[node] = count
            return count

        max_color_value = 0
        for node in range(n):
            result = dfs(node)
            if has_cycle:
                return -1
            max_color_value = max(max_color_value, max(result))

        return max_color_value
