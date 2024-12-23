from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1) # from zero to amount , for ex1 :[12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
        dp[0] = 0 
        for a in range(1,amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a],1+dp[a-c])
                    # if coin = 4 , a = 7 , dp[7] = 1+dp[3]
        return dp[amount] if dp[amount] != amount +1 else -1  

        

        
        # cache = {}

        # # Helper function for depth-first search
        # def dfs(remaining):
        #     if remaining == 0:
        #         return 0  # No coins needed
        #     if remaining < 0:
        #         return float('inf')  # Impossible case
        #     if remaining in cache:
        #         return cache[remaining]

        #     # Try every coin and calculate the minimum
        #     min_coins = float('inf')
        #     for coin in coins:
        #         result = dfs(remaining - coin)
        #         if result != float('inf'):
        #             min_coins = min(min_coins, 1 + result)  # 1 is the number of coin not value 

        #     # Store result in cache
        #     cache[remaining] = min_coins
        #     return cache[remaining]

        # result = dfs(amount)
        # return result if result != float('inf') else -1
