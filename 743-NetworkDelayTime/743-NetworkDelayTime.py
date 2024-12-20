import collections
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create a graph representation using adjacency list
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))  # Add an edge from u to v with weight w

        # Min-heap to store (time, node), initialized with the starting node
        minHeap = [(0, k)]
        
        # Set to keep track of visited nodes
        visit = set()
        
        # Variable to store the maximum time taken to reach any node
        t = 0

        # Process the nodes in order of increasing time
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)  # Get the node with the smallest time
            if n1 in visit:
                continue  # Skip if the node is already visited

            # Mark the node as visited and update the time
            visit.add(n1)
            t = max(t, w1)

            # Traverse all neighbors of the current node
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    # Add the neighbor to the heap with the updated time
                    heapq.heappush(minHeap, (w1 + w2, n2))

        # If all nodes are visited, return the maximum time, otherwise return -1
        return t if len(visit) == n else -1
