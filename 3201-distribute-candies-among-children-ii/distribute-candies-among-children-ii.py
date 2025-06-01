class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(min(n, limit) + 1):
            # For fixed a = i, compute valid b range
            min_b = max(0, n - i - limit)
            max_b = min(limit, n - i)
            if max_b >= min_b:
                res += (max_b - min_b + 1)
        return res

        
        