from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        # Helper function for depth-first search
        def dfs(remaining):
            if remaining == 0:
                return 0  # No coins needed
            if remaining < 0:
                return float('inf')  # Impossible case
            if remaining in cache:
                return cache[remaining]

            # Try every coin and calculate the minimum
            min_coins = float('inf')
            for coin in coins:
                result = dfs(remaining - coin)
                if result != float('inf'):
                    min_coins = min(min_coins, 1 + result)  # 1 is the number of coin not value 

            # Store result in cache
            cache[remaining] = min_coins
            return cache[remaining]

        result = dfs(amount)
        return result if result != float('inf') else -1
