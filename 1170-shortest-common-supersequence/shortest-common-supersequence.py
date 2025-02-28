class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # lcs between str1[i:] and str2[j:] (for all (i, j)) by using dynamic programming.
        # abac - cab 
        # lcs : ab 
        # 1st ac 
        # 2nd c 
        # 2nd + lcs(1st,2nd)+ 1st 

        dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

        for i in range(len(str1) - 1, -1, -1):
            for j in range(len(str2) - 1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]  # Go diagonally when characters match
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])  # Max of down or right

        # Reconstruct the LCS
        res = []
        i, j = 0, 0
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                res.append(str1[i])
                i += 1
                j += 1
            elif dp[i + 1][j] >= dp[i][j + 1]:
                i += 1
            else:
                j += 1

        common = ''.join(res)

        # Build the Shortest Common Supersequence
        i, j = 0, 0
        scs = []

        for c in common:
            # Add non-LCS characters from str1
            while i < len(str1) and str1[i] != c:
                scs.append(str1[i])
                i += 1

            # Add non-LCS characters from str2
            while j < len(str2) and str2[j] != c:
                scs.append(str2[j])
                j += 1

            # Add the common character
            scs.append(c)
            i += 1
            j += 1

        # Add any remaining characters
        scs.append(str1[i:])
        scs.append(str2[j:])

        return ''.join(scs)



        
        
        