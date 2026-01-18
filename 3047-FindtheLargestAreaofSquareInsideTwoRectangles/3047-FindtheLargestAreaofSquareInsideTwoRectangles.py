# Last updated: 1/18/2026, 2:27:24 PM
1class Solution:
2    def largestSquareArea(
3        self, bottomLeft: List[List[int]], topRight: List[List[int]]
4    ) -> int:
5        max_size = 0
6
7        for (bottom_left_i, top_right_i), (
8            bottom_left_j,
9            top_right_j,
10        ) in combinations(zip(bottomLeft, topRight), 2):
11            w = min(top_right_i[0], top_right_j[0]) - max(
12                bottom_left_i[0], bottom_left_j[0]
13            )
14            h = min(top_right_i[1], top_right_j[1]) - max(
15                bottom_left_i[1], bottom_left_j[1]
16            )
17
18            max_size = max(max_size, min(w, h))
19
20        return max_size * max_size