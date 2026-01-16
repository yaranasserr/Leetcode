# Last updated: 1/16/2026, 2:42:54 PM
1class Solution:
2    def get_edges(self, fences: List[int], border: int) -> set:
3        points = sorted([1] + fences + [border])
4        return {
5            points[j] - points[i]
6            for i in range(len(points))
7            for j in range(i + 1, len(points))
8        }
9
10    def maximizeSquareArea(
11        self, m: int, n: int, hFences: List[int], vFences: List[int]
12    ) -> int:
13        MOD = 10**9 + 7
14        h_edges = self.get_edges(hFences, m)
15        v_edges = self.get_edges(vFences, n)
16
17        max_edge = max(h_edges & v_edges, default=0)
18        return (max_edge * max_edge) % MOD if max_edge else -1