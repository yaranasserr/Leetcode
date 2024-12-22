class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp={}# cache
        # i : index of days 

        def dfs(i):
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]

            dp[i] = float("inf")# minimum no
            #d: no of days you can travel , c : cost for travelling in this days
            for d , c in zip([1,7,30],costs):
                j = i
                # check the first day that will be out of bounce
                while j< len(days) and days[j]< days[i]+d : 
                    j+=1 

                dp[i] = min(dp[i],c+dfs(j)) # i : index of current day , d:pervious days


            return dp[i]

        return dfs(0)






        