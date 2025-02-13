class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def freq(word):
            freq= {}
            for w in word :
                freq[w] = freq.get(w, 0) + 1 
            return freq

    

        freqs=freq(s)
        freqt=freq(t)
        return freqs==freqt
        
   