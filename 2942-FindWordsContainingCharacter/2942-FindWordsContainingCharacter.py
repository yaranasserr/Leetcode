# Last updated: 5/24/2025, 1:38:51 PM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]

  