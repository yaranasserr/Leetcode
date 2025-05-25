from typing import List
from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = Counter(words)
        length = 0
        used_middle = False

        for word in list(freq.keys()):
            rev = word[::-1]

            if word == rev:
                # Symmetric word (like "aa")
                pairs = freq[word] // 2
                length += pairs * 4
                freq[word] -= pairs * 2
            else:
                # Pair with its reverse
                if rev in freq:
                    pairs = min(freq[word], freq[rev])
                    length += pairs * 4
                    freq[word] -= pairs
                    freq[rev] -= pairs

        # Check if any symmetric word remains for the center
        for word in freq:
            if word[0] == word[1] and freq[word] > 0:
                length += 2
                break

        return length
