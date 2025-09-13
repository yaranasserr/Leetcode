class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = {}
        for ch in s :
            freq[ch] = 1 +freq.get(ch,0)

        vowels = "aeiou"

        max_vowel = max((freq[key] for key in freq if key in vowels), default=0)
        max_con = max((freq[key] for key in freq if key not in vowels),default=0)

        return max_vowel +max_con
        