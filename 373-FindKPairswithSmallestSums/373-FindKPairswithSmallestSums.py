# Last updated: 7/27/2025, 4:49:30 PM
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp={}
        def solve(i,flag,count):
            if i>=len(prices) or count>=k:
                return 0
            if (i,flag,count) in dp:
                return dp[(i,flag,count)]
            if flag:
                buy=-prices[i]+solve(i+1,False,count)
                skip=solve(i+1,True,count)
                dp[(i,flag,count)]=max(buy,skip)
            else:
                sell=prices[i]+solve(i+1,True,count+1)
                hold=solve(i+1,False,count)
                dp[(i,flag,count)]=max(sell,hold)
            return dp[(i,flag,count)]
        return solve(0,True,0)