class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Initialize the cache with dimensions len(word1)+1 x len(word2)+1
        cache = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        
        # Fill the base cases for the cache
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i
        
        # Fill the cache using bottom-up dynamic programming
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1])
        # min(insert,delete,replace)
        return cache[0][0]
