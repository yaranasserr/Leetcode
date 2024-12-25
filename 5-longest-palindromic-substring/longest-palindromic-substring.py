class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        reslen=0

        for i in range(len(s)):
            # odd length 
            l,r = i , i  # i is center position
            while l >= 0 and r < len(s) and s[l] == s[r] :
                if (r-l+1) > reslen:
                    res = s[l:r+1]
                    reslen = r-l +1
                l -=1
                r +=1

            # even length
            l , r = i , i+1
            while l >=  0 and r < len(s) and s[l] == s[r] :
                if (r-l+1) > reslen:
                    res = s[l:r+1]
                    reslen =r-l +1
                l -=1
                r +=1

        return res


# Iteration (i)	Center Character (s[i])	Odd Length Check (l = r = i)	Even Length Check (l = i, r = i+1)	Updates to res and reslen
# 0	'b'	Odd: l = 0, r = 0 → "b"	Even: l = 0, r = 1 → no change	res = "b", reslen = 1
# 1	'a'	Odd: l = 1, r = 1 → "a"	Even: l = 1, r = 2 → no change	No change
# Odd: l = 0, r = 2 → "bab"	Even: l = 1, r = 2 → no change	res = "bab", reslen = 3
# 2	'b'	Odd: l = 2, r = 2 → "b"	Even: l = 2, r = 3 → no change	No change
                

        