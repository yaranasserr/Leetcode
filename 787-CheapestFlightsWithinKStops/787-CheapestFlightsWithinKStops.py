class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # shortest path fatser algo 
        prices =[float("inf")]*n
        prices[src] = 0 
       # Build the adjacency list

        adj = [[] for _ in range(n)]
        for s, d, cost in flights:
            adj[s].append((d, cost))

        q = deque([(0,src,0)])
        while q :
            cst , node , stops = q.popleft()
            if stops > k :
                continue

            for nei , w in adj[node]:
                nextcost = cst+ w 
                if nextcost < prices[nei]:
                    prices[nei] = nextcost 
                    q.append((nextcost,nei,stops+1))

        return prices[dst] if prices[dst] != float("inf") else -1
        
        # # Min-heap: (cost, current city, remaining stops)
        # heap = [(0, src, k + 1)] #  stops count edges, not nodes
        
        # # Dijkstra-like approach
        # while heap:
        #     cost, city, stops = heapq.heappop(heap)
            
        #     if city == dst:
        #         return cost
            
        #     if stops > 0:
        #         for neighbor, price in adj[city]:
        #             heapq.heappush(heap, (cost + price, neighbor, stops - 1))
        
        # return -1