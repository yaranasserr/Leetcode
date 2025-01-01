class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        
        if not prices:
            return 0

        k = 2  # Maximum number of transactions
        n = len(prices)
        dp = [[0] * n for _ in range(k + 1)]

        for t in range(1, k + 1):
            maxDiff = -prices[0]
            for i in range(1, n):
                dp[t][i] = max(dp[t][i-1], prices[i] + maxDiff)
                maxDiff = max(maxDiff, dp[t-1][i] - prices[i])

        return dp[k][n-1]
