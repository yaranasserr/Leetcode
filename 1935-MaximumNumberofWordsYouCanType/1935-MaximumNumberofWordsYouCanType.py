# Last updated: 9/15/2025, 12:03:06 PM
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        brokenLetters = list(brokenLetters)

        count = sum(1 for word in words if any(ch in word for ch in brokenLetters))
        return len(words) - count
