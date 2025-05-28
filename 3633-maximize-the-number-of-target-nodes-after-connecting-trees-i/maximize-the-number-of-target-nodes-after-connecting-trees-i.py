from collections import defaultdict, deque
from typing import List

class Solution:
    def bfs_within_k(self, graph, start, k):
        visited = set()
        queue = deque([(start, 0)])
        count = 0
        while queue:
            node, dist = queue.popleft()
            if node in visited or dist > k:
                continue
            visited.add(node)
            count += 1
            for neighbor in graph[node]:
                queue.append((neighbor, dist + 1))
        return count

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        tree1 = defaultdict(list)
        tree2 = defaultdict(list)
        n = len(edges1) + 1
        m = len(edges2) + 1

        # Build the graphs
        for a, b in edges1:
            tree1[a].append(b)
            tree1[b].append(a)
        for u, v in edges2:
            tree2[u].append(v)
            tree2[v].append(u)

        # Precompute reachable nodes in tree2 for all nodes (within distance k)
        reach_tree2 = []
        for node in range(m):
            reach_tree2.append(self.bfs_within_k(tree2, node, k - 1))  # since 1 edge will be used for connection

        max_reach_in_tree2 = max(reach_tree2)

        # Now for each node in tree1, compute reachable within k
        result = []
        for i in range(n):
            reach1 = self.bfs_within_k(tree1, i, k)
            result.append(reach1 + max_reach_in_tree2)

        return result
