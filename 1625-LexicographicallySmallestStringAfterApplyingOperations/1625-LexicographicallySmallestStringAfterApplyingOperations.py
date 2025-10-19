# Last updated: 10/19/2025, 3:18:12 PM
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # graph - dfs 
        n = len(s)
        incremented={str(n):str((n+a)%10) for n in range(10)} # for cycling
        # {'0': '9', '1': '0', '2': '1', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6', '8': '7', '9': '8'}

        def add(s):
            res = ""
            for i in range(n):
                res+= s[i] if i%2 == 0 else incremented[s[i]] # if even index , dont add , otherwise take the num from increment
            return res 

        def rotate(s):
            return s[n-b:] +s[:n-b]

        seen = set()

        def dfs(s):
            if s in seen :
                return 

            seen.add(s)
            dfs(add(s))
            dfs(rotate(s))

            return 

        dfs(s)

        return min(seen)





        
        