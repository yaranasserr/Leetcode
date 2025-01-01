from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}

        def dfs(i):
            if i in safe:
                return safe[i]

            safe[i] = False  # Mark as visiting
            for nei in graph[i]:
                if not dfs(nei):
                    return False  # If any neighbor is not safe, this node is not safe
            
            safe[i] = True  # Mark as safe after all neighbors are confirmed safe
            return safe[i]

        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res
