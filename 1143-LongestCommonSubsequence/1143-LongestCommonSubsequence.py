class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]

        for i  in range((len(text1)-1),-1,-1):
            for j  in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1+dp[i+1][j+1]
                else :
                    dp[i][j] = max(dp[i+1][j] , dp[i][j+1])
        return dp[0][0]

























        # dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # for i in range(len(text1)-1,-1,-1):

        #     for j in range(len(text2)-1,-1,-1):

        #         if text1[i]==text2[j]:

        #             dp[i][j]= 1+ dp[i+1][j+1] # add one to the diagonal
                    
        #         else:
        #             dp[i][j] = max(dp[i][j+1],dp[i+1][j]) # max( the right ,bottom)
        # return dp[0][0]
        
# i = 4, text1[4] = 'e':
# j = 2, text2[2] = 'e': Match! So, dp[4][2] = 1 + dp[5][3] = 1.
# j = 1, text2[1] = 'c': No match, so dp[4][1] = max(dp[4][2], dp[5][1]) = 1.
# j = 0, text2[0] = 'a': No match, so dp[4][0] = max(dp[4][1], dp[5][0]) = 1.
# Updated dp:

# dp = [[0, 0, 0, 0],
#       [0, 0, 0, 0],
#       [0, 0, 0, 0],
#       [0, 0, 0, 0],
#       [1, 1, 1, 0],
#       [0, 0, 0, 0]]
# i = 3, text1[3] = 'd':
# j = 2, text2[2] = 'e': No match, so dp[3][2] = max(dp[3][3], dp[4][2]) = 1.
# j = 1, text2[1] = 'c': No match, so dp[3][1] = max(dp[3][2], dp[4][1]) = 1.
# j = 0, text2[0] = 'a': No match, so dp[3][0] = max(dp[3][1], dp[4][0]) = 1.

# dp = [[0, 0, 0, 0],
#       [0, 0, 0, 0],
#       [0, 0, 0, 0],
#       [1, 1, 1, 0],
#       [1, 1, 1, 0],
#       [0, 0, 0, 0]]
# i = 2, text1[2] = 'c':
# j = 2, text2[2] = 'e': No match, so dp[2][2] = max(dp[2][3], dp[3][2]) = 1.
# j = 1, text2[1] = 'c': Match! So, dp[2][1] = 1 + dp[3][2] = 2.
# j = 0, text2[0] = 'a': No match, so dp[2][0] = max(dp[2][1], dp[3][0]) = 2.

# dp = [[0, 0, 0, 0],
#       [0, 0, 0, 0],
#       [2, 2, 1, 0],
#       [1, 1, 1, 0],
#       [1, 1, 1, 0],
#       [0, 0, 0, 0]]
# i = 1, text1[1] = 'b':
# j = 2, text2[2] = 'e': No match, so dp[1][2] = max(dp[1][3], dp[2][2]) = 1.
# j = 1, text2[1] = 'c': No match, so dp[1][1] = max(dp[1][2], dp[2][1]) = 2.
# j = 0, text2[0] = 'a': No match, so dp[1][0] = max(dp[1][1], dp[2][0]) = 2.

# dp = [[0, 0, 0, 0],
#       [2, 2, 1, 0],
#       [2, 2, 1, 0],
#       [1, 1, 1, 0],
#       [1, 1, 1, 0],
#       [0, 0, 0, 0]]
# i = 0, text1[0] = 'a':
# j = 2, text2[2] = 'e': No match, so dp[0][2] = max(dp[0][3], dp[1][2]) = 1.
# j = 1, text2[1] = 'c': No match, so dp[0][1] = max(dp[0][2], dp[1][1]) = 2.
# j = 0, text2[0] = 'a': Match! So, dp[0][0] = 1 + dp[1][1] = 3.
# Final dp:

# dp = [[3, 2, 1, 0],
#       [2, 2, 1, 0],
#       [2, 2, 1, 0],
#       [1, 1, 1, 0],
#       [1, 1, 1, 0],
#       [0, 0, 0, 0]]


        