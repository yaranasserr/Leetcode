# Last updated: 3/29/2025, 12:29:12 PM
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtrack(i):
            # i index 
            if i == len(s):
                res.append(" ".join(cur))
                return

            for j in range(i,len(s)):
                w=s[i:j+1]
                if w in wordDict :
                    cur.append(w)
                    backtrack(j+1)
                    cur.pop()

        cur=[]
        res=[]
        backtrack(0)
        return res
        # def backtrack(start, path):
        #     if start == len(s):
        #         final.append(" ".join(path))
        #         return

        #     for word in wordDict:
        #         if s[start:start+len(word)] == word:
        #             backtrack(start + len(word), path + [word])

        # final = []
        # backtrack(0, [])
        # return final

    # O(2 ** n)
