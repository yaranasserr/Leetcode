from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n 

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Disjoint Set Union
        uf = UnionFind(n)

        # Step 1: Build components
        for u, v, w in edges:
            uf.union(u, v)

        # Step 2: Compute the minimum cost of each component
        component_cost = {}  # root -> minimum cost
        for u, v, w in edges:
            root = uf.find(u)
            if root not in component_cost:
                component_cost[root] = w
            else:
                component_cost[root] &= w

        # Step 3: Answer queries
        res = []
        for src, dst in queries:
            r1, r2 = uf.find(src), uf.find(dst)
            if r1 != r2:
                res.append(-1)
            else:
                res.append(component_cost[r1])
        return res
