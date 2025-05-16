# Last updated: 5/16/2025, 6:54:20 PM
from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def hamming_distance(s1, s2):
            count = 0 
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    count += 1
            return count 
        
        n = len(words)
        if n == 0:
            return []

        dp = [1] * n 
        prev = [-1] * n 
        max_len = 1
        end_idx = 0 

        for i in range(n):
            for j in range(i):
                # check rules 
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    if hamming_distance(words[i], words[j]) == 1:
                        if dp[j] + 1 > dp[i]:
                            dp[i] = dp[j] + 1
                            prev[i] = j 

                        if dp[i] > max_len:
                            max_len = dp[i] 
                            end_idx = i 

        res_seq = []
        curr = end_idx
        while curr != -1:
            res_seq.append(words[curr])
            curr = prev[curr]

        return res_seq[::-1]
