from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:

        freq = Counter(s)
        delete = 0
        for key  in freq.values():
            # odd : remove all but one 
            if key % 2 != 0 :
                delete += key -1 
            # even :
            else :
                delete += key -2 

        return len(s) - delete



        # filtered = ((key, val) for key, val in freq.items() if val >= 3)

        # for key, val in= filtered:
        #     while val >= 3:
            
        #         l = word_list.index(key)
        #         r  = len(word_list) - 1 - word_list[::-1].index(key)

        #         word_list.pop(r)  
        #         word_list.pop(l)  
             
        #         val -= 2

       
        # result = ''.join(word_list)
        # return len(result)
