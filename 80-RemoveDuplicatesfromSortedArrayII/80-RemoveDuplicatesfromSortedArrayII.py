# Last updated: 7/9/2025, 2:49:16 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def frequency(w):
            freq = {}
            for i in w :
                freq[i] = 1+freq.get(i,0)
            return freq 

        freqs = frequency(s)
        freqt = frequency(t)

        return freqs==freqt

        