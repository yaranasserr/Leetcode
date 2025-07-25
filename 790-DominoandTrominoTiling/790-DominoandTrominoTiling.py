# Last updated: 5/5/2025, 3:00:51 PM
class Solution:
    def numTilings(self, n: int) -> int:
        # dynamic programming 
        # note: F = Full, T = TopMissing, B = BottomMissing

        F = {0: 1, 1: 1}
        T = {1: 0}
        B = {1: 0}

        for i in range(2, n + 1): 
            F[i] = F[i - 1] + F[i - 2] + T[i - 1] + B[i - 1]
            T[i] = F[i - 2] + B[i - 1]
            B[i] = F[i - 2] + T[i - 1]

        return F[n] % (10 ** 9 + 7)