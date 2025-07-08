from bisect import bisect_right
from functools import lru_cache

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by start day
        events.sort()

        # Extract start times for binary search
        start_times = [e[0] for e in events]

        @lru_cache(None)
        def dfs(i, remaining_k):
            if i == len(events) or remaining_k == 0:
                return 0

            # Option 1: skip the current event
            res = dfs(i + 1, remaining_k)

            # Option 2: take the current event
            # Find next event that starts after events[i][1]
            next_index = bisect_right(start_times, events[i][1])
            res = max(res, events[i][2] + dfs(next_index, remaining_k - 1))

            return res

        return dfs(0, k)
