from collections import deque
from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        def bfs(start): 
            q = deque([(start, 0)])
            visit = {}
            while q:
                node, distance = q.popleft()
                if node in visit:
                    continue
                visit[node] = distance
                nei = edges[node]
                if nei != -1 and nei not in visit:
                    q.append((nei, distance + 1))
            return visit
        
        dist1 = bfs(node1)
        dist2 = bfs(node2)

        result = -1
        min_dist = float('inf')
        
        for i in range(len(edges)):
            if i in dist1 and i in dist2:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_dist:
                    min_dist = max_dist
                    result = i
                    
        return result
