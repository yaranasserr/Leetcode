from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Step 1: DFS to map each node to its parent
        parent_map = {}

        def dfs(root, parent_map, parent=None):
            if not root:
                return
            parent_map[root] = parent  
            dfs(root.left, parent_map, root)
            dfs(root.right, parent_map, root)

        def build_adj_list(root):
            dfs(root, parent_map)
            adj = {node: [] for node in parent_map}

            for node, parent in parent_map.items():
                if parent:
                    adj[node].append(parent)
                    adj[parent].append(node)

            return adj

        # Step 2: Build adjacency list
        adj_list = build_adj_list(root)

        # Step 3: BFS from the Target Node
        res = []
        def bfs(adj, target, k):
            q = deque([(target, 0)])  # (node, distance)
            visit = set()
            visit.add(target)

            while q:
                node, length = q.popleft()
                if length == k:
                    res.append(node.val)  # Store the node value
                elif length < k:
                    for neighbor in adj.get(node, []):
                        if neighbor not in visit:
                            visit.add(neighbor)
                            q.append((neighbor, length + 1))

        bfs(adj_list, target, k)
        return res
