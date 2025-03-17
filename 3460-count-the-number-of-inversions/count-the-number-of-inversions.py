from typing import List

class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        r = {e: c for e,c in requirements}
        c = max(r.values())
        max_end = max(r)
        mod = 10 ** 9 + 7
        dp = [1] + [0] * c
        for i in range(max_end + 1):
            dp2 = [0] * (c + 1)
            if i in r:
                dp2[r[i]] = sum(dp[max(0, r[i] - i): r[i] + 1]) % mod
            else:
                for j in range(c + 1):
                    dp2[j] = dp[j]
                    if j: dp2[j] += dp2[j - 1]
                    if j - i > 0: dp2[j] -= dp[j - i - 1]
            dp = dp2
        res = sum(dp) % mod
        for i in range(max_end + 1, n):
            res = res * (i + 1) % mod
        return res