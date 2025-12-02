# Last updated: 12/2/2025, 2:47:32 PM
1class Solution:
2    def countTrapezoids(self, points: List[List[int]]) -> int:
3        point_num = defaultdict(int)
4        mod = 10**9 + 7
5        ans, total_sum = 0, 0
6        for point in points:
7            point_num[point[1]] += 1
8        for p_num in point_num.values():
9            edge = p_num * (p_num - 1) // 2
10            ans = (ans + edge * total_sum) % mod
11            total_sum = (total_sum + edge) % mod
12        return ans