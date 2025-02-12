class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def freq(word):
            freq= {}
            for w in word :
                freq[w] = freq.get(w, 0) + 1 
            return freq

        freq1=freq(ransomNote)
        freq2=freq(magazine)

        for char in freq1:
            if freq1[char] > freq2.get(char, 0):  # If not enough letters in magazine
                return False

        return True
      
                
  