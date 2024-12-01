class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        # Initial states
        cash = 0  # Max profit with no stock in hand
        hold = -prices[0]  # Max profit with stock in hand (bought at prices[0])

        for i in range(1, n):
            # Update cash and hold
            cash = max(cash, hold + prices[i] - fee)  # Sell the stock or do nothing
            hold = max(hold, cash - prices[i])  # Buy a stock or do nothing

        return cash



        # res = 0
        # buy , sell = 0 ,0
        # for i in range(len(prices)):
        #     sell =max(sell,prices[i])
        #     buy=min(buy,prices[i])
        #     res+= (sell - buy - fee)
        # return res


        