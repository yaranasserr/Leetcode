class Solution:
    def numDecodings(self, s: str) -> int:
        # letter_mapping = {str(i): chr(64 + i) for i in range(1, 27)}
        #dp o(n) time 0(1) memory
        dp = {len(s):1} # if it is empty return 1

        for i in range(len(s)-1,-1,-1):
            if s[i] =="0":
                dp[i] =0  #base Case
            else:
                dp[i]=dp[i+1]

            if (i+1 < len(s) and (s[i]=="1" or s[i] =="2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]

        return dp[0]




        