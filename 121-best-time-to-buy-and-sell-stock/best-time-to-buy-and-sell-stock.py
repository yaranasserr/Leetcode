class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0 
        min_price =float('inf')
        for p in prices :
            if p < min_price :
                min_price = p 
            else:
                total = max(total , p - min_price )

        return total 

        