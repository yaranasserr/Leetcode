# Last updated: 12/22/2025, 6:03:35 PM
1class Solution(object):
2    def minDeletionSize(self, A):
3        W = len(A[0])
4        dp = [1] * W
5        for i in xrange(W-2, -1, -1):
6            for j in xrange(i+1, W):
7                if all(row[i] <= row[j] for row in A):
8                    dp[i] = max(dp[i], 1 + dp[j])
9
10        return W - max(dp)