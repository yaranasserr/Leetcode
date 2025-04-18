class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestCommonSubsequence(s,s[::-1])

    def longestCommonSubsequence(self, s1: str , s2:str) -> int:
            
        dp = [[0]* (len(s1)+1) for _ in range(len(s2)+1)]

        for i in range((len(s1)-1),-1,-1):
            for j in range((len(s2)-1),-1,-1):
                if s1[i] == s2[j]:
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j] , dp[i][j+1])

        return dp[0][0]




        