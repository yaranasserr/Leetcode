# Last updated: 12/23/2025, 3:56:12 PM
1class Solution:
2    def maxTwoEvents(self, events: List[List[int]]) -> int:
3
4        end_sorted = deque(sorted(events, key=itemgetter(1)))
5        start_sorted = sorted(events, key=itemgetter(0))
6
7        ans = max(v for _, _, v in events)
8
9        end_max = 0  
10
11        for start, end, value in start_sorted:
12            while end_sorted and end_sorted[0][1] < start:
13                _, _, v = end_sorted.popleft()
14                end_max = max(end_max, v)
15            ans = max(ans, value + end_max)
16
17        return ans