# Last updated: 12/18/2025, 3:34:07 PM
1class Solution:
2    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
3        n = len(prices)
4        profitSum = [0] * (n + 1)
5        priceSum = [0] * (n + 1)
6        for i in range(n):
7            profitSum[i + 1] = profitSum[i] + prices[i] * strategy[i]
8            priceSum[i + 1] = priceSum[i] + prices[i]
9        res = profitSum[n]
10        for i in range(k - 1, n):
11            leftProfit = profitSum[i - k + 1]
12            rightProfit = profitSum[n] - profitSum[i + 1]
13            changeProfit = priceSum[i + 1] - priceSum[i - k // 2 + 1]
14            res = max(res, leftProfit + changeProfit + rightProfit)
15        return res