# Last updated: 7/27/2025, 2:16:16 PM
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        # Step 1: Create a list of projects (capital, profit)
        projects = list(zip(capital, profits))
        
        # Step 2: Create a min-heap sorted by capital
        min_capital_heap = []
        for c, p in projects:
            heapq.heappush(min_capital_heap, (c, p))
        
        # Step 3: Max-heap for available projects (use negative profits because Python heapq is a min-heap)
        max_profit_heap = []
        
        # Step 4: Try to select up to k projects
        for _ in range(k):
            # Move all projects that can be afforded to max-profit heap
            while min_capital_heap and min_capital_heap[0][0] <= w:
                c, p = heapq.heappop(min_capital_heap)
                heapq.heappush(max_profit_heap, -p)
            
            # If no project can be afforded, stop
            if not max_profit_heap:
                break
            
            # Do the most profitable project
            w += -heapq.heappop(max_profit_heap)
        
        return w
