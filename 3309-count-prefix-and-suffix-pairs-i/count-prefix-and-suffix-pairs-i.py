class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res=[]

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] == words[j][0:len(words[i])] and words[i] == words[j][-len(words[i]):]:
                    res.append(1)  

      
 
        return len(res)

        