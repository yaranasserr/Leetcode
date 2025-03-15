class Solution:
    def largestVariance(self, s: str) -> int:
        counter = collections.Counter(s)
        res = 0 
        for char1 , char2 in itertools.permutations(counter,2):
        
            char1_count = counter[char1]
            char2_count = counter[char2]
            diff = 0 
            seen_char1 = seen_char2 = False 
            # maximum of ( char1 - char2 ) when char1 is >>> char2 
            # assume char1 is greater 
            for char in s :
                if char not in (char1,char2):
                    continue 

                if diff < 0 :
                    # is there more char1 in string 
                    if not char1_count :
                        break
                    if not char2_count :
                        res = max(res,diff+char1_count)

                        break 

                    seen_char1 = seen_char2 = False 
                    diff = 0 

                if char == char1 :
                    seen_char1 = True 
                    char1_count -=1 
                    diff +=1 

                if char == char2 :
                    seen_char2=True
                    char2_count  -=1 
                    diff -=1 

                if seen_char1 and seen_char2 :
                    res = max(res,diff)

        return res


        

"""
Counter({'b': 4, 'a': 3}) 

1st iteration (char1 = 'a', char2 = 'b'):

char1_count = counter['a'] = 3
char2_count = counter['b'] = 4
2nd iteration (char1 = 'b', char2 = 'a'):

char1_count = counter['b'] = 4
char2_count = counter['a'] = 3

"""

        