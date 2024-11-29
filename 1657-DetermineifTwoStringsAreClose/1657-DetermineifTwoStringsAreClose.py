from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Check if the sets of characters in both strings are the same
        if set(word1) != set(word2):
            return False
        
        # Check if the frequency distributions of characters in both strings are the same
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())
