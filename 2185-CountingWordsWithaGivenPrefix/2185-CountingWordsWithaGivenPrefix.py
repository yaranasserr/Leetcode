class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        count = 0 
        for i in range(len(words)):
            # print(words[i][0:n+1])
            if words[i][0:n] == pref  :

                count +=1 

        return count 
            
        