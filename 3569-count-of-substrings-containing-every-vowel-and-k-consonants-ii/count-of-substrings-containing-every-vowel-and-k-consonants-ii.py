class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        def atleastk(k):
            vowel=defaultdict(int)
            non_vowel=0 
            res = 0 
            l = 0 
            for r in range(len(word)):
                if word[r] in "aeiou":
                    vowel[word[r]]+=1
                else:
                    non_vowel+=1
                while len(vowel) == 5 and non_vowel >= k :
                    res+=( len(word) - r)

                    if word[l] in "aeiou":
                        vowel[word[l]] -=1 
                    else:
                        non_vowel -=1

                    if vowel[word[l]] == 0 :
                        vowel.pop(word[l])

                    l+=1

            return  res

        return atleastk(k) - atleastk(k+1)




        # vowels = set('aeiou')
        # # sliding window its max length = 5 + k 
        # # check what inside the window if it contains the 5 vowels and k not vowels 
        # window_length = 5 + k 

        # res = 0 
        # if len(word)< window_length :
        #     return 0 

        # for i in range(len(word)-window_length+1):
        #     window=word[i:i+window_length]
        #     current_vowels = set()
        #     c_count = 0 

        #     for ch in window:
        #         if ch in vowels:
        #             current_vowels.add(ch)
        #         else:
        #             c_count +=1

        #     if len(current_vowels)==5 and c_count >= k :
        #         res+=1
        #     if c_count > k :
        #         break

        # return res 
                



  
     
        






        

        
        






        

        