class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        one = len(word1)
        two = len(word2)
        dp =[[0]*(two+1) for _ in range(one+1)]
        # base case empty w2 and w1 is full , last column 
        for r in range(one+1):
            dp[r][two] = one - r 

        # base case empty w1 and w2 is full , last row 
        for c in range(two+1):
            dp[one][c]=two - c 

        for i in range(one-1,-1,-1):
            for j in range(two-1,-1,-1):
                # if they are equal skip 
                if word1[i]==word2[j]:
                    # move diagonal 
                    dp[i][j]= dp[i+1][j+1]
                else:
                    dp[i][j]= 1+min(dp[i][j+1],dp[i+1][j],dp[i+1][j+1])
        return dp[0][0]

 