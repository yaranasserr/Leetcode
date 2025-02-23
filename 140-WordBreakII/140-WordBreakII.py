from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtrack(start, path):
            if start == len(s):
                final.append(" ".join(path))
                return

            for word in wordDict:
                if s[start:start+len(word)] == word:
                    backtrack(start + len(word), path + [word])

        final = []
        backtrack(0, [])
        return final
