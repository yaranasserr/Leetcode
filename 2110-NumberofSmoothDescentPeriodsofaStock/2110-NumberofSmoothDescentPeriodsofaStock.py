# Last updated: 12/15/2025, 10:40:42 PM
1class Solution:
2    def getDescentPeriods(self, prices: List[int]) -> int:
3        n = len(prices)
4        res = 1  # total number of smooth descending periods, initial value is dp[0]
5        prev = 1  # total number of smooth descending periods ending with the previous element, initial value is dp[0]
6        # traverse the array starting from 1, and update prev and the total res according to the recurrence relation
7        for i in range(1, n):
8            if prices[i] == prices[i - 1] - 1:
9                prev += 1
10            else:
11                prev = 1
12            res += prev
13        return res