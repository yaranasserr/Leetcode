class Solution:
   # def dp(int i ,int costSf , int cost):
        
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2,len(cost)):
            cost[i] += min(cost[i-1],cost[i-2])
        return min(cost[-2],cost[-1])
        