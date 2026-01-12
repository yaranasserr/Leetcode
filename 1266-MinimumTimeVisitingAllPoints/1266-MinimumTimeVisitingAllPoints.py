# Last updated: 1/12/2026, 6:47:34 PM
1class Solution:
2    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
3        ans = 0
4        for i in range(len(points) - 1):
5            curr_x, curr_y = points[i]
6            target_x, target_y = points[i + 1]
7            ans += max(abs(target_x - curr_x), abs(target_y - curr_y))
8        
9        return ans