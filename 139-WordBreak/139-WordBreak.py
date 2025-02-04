class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True # base case

        for i  in range(len(s)-1 , -1 ,-1):
            for w in wordDict:
                # there are enough chars in s to compare them 
                if (i+len(w)) <= len(s) and s[i:i+len(w)]==w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
                 


        
        