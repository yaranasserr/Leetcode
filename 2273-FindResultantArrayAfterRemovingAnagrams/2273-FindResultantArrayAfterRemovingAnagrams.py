# Last updated: 10/13/2025, 12:25:57 PM
from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]  # always keep the first word

        for i in range(1, len(words)):
            if sorted(words[i]) != sorted(res[-1]):
                res.append(words[i])
        
        return res
