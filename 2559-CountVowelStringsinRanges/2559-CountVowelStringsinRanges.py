# class Solution:
#     def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # vowels = list("aeoui")
        # res = []
        

        
        # for q in queries :
        #     count = 0
        #     sub = words[q[0]:q[1]+1]
        #     for w in sub :
        #          if w[0] in vowels and w[-1] in vowels:
        #             count +=1 
           
        #     res.append(count)

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        # Precompute a prefix sum array
        n = len(words)
        prefix = [0] * (n + 1)
        
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]
        
        # Use the prefix sum to quickly answer queries
        res = []
        for li, ri in queries:
            res.append(prefix[ri + 1] - prefix[li])
        
        return res


          
            


                
         

        
  

        