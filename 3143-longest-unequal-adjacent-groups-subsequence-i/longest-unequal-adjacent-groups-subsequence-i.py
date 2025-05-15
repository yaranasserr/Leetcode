class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        return [ words[0] ]+ [words[i] for i in range(1,n) if groups[i]!= groups[i-1]]
        # res = []
        # n = len(words)
        # if n == 1 :
        #     return words 
        # if n==2 and groups[0] == groups[1]:
        #     return [words[0]]
        
        # for i in range(n):
        #     if groups[i] != groups[i-1] :
        #         res.append(words[i])

        # return res 

        