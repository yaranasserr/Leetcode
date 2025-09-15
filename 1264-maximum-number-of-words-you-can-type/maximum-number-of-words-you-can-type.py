class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        return len(text.split())- sum(1 for word in text.split() if any(ch in word for ch in list(brokenLetters)))
 
