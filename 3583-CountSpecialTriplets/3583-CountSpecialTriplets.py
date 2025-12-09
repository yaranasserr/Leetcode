# Last updated: 12/9/2025, 11:30:24 AM
1class Solution:
2    def specialTriplets(self, nums: List[int]) -> int:
3        MOD = 10**9 + 7
4        num_cnt = {}
5        num_partial_cnt = {}
6
7        for v in nums:
8            num_cnt[v] = num_cnt.get(v, 0) + 1
9
10        ans = 0
11        for v in nums:
12            target = v * 2
13            l_cnt = num_partial_cnt.get(target, 0)
14            num_partial_cnt[v] = num_partial_cnt.get(v, 0) + 1
15            r_cnt = num_cnt.get(target, 0) - num_partial_cnt.get(target, 0)
16            ans = (ans + l_cnt * r_cnt) % MOD
17
18        return ans